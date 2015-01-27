from .models import Invoice, Transaction
from .serializers import InvoiceSerializer
from rest_framework import generics, status
from django.db import transaction as transaction_control
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


class InvoiceList(APIView):
    def get(self, request, format=None):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            invoice = self.save_invoice(data)
            response_serializer = InvoiceSerializer(invoice)
            return Response(response_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save_invoice(self, data):
        transaction_list = data.get('transactions')
        customer = data.get('customer')
        with transaction_control.atomic():
            inv = Invoice(customer=customer)
            inv.save()
            for t in transaction_list:
                product = t.get('product')
                quantity = t.get('quantity')
                price = t.get('price')
                transact = Transaction(invoice=inv,
                                       product=product,
                                       quantity=quantity, price=price)
                transact.save()
            inv.save()
        return inv


class InvoiceDetail(APIView):

    def get_object(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise Http404

    def update_invoice(self, data):
        transaction_list = data.get('transactions')
        with transaction_control.atomic():
            inv = self.get_object(data.get('id'))
            for t in transaction_list:
                print t
                id = t.get('id')
                transact = Transaction(pk=id)
                transact.price = t.get('price')
                transact.product = t.get('product')
                transact.quantity = t.get('quantity')
                transact.invoice = inv
                transact.save()
            inv.save()
        return inv

    def get(self, request, pk, format=None):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        invoice = self.get_object(pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            invoice = self.update_invoice(request.data)
            response_serializer = InvoiceSerializer(invoice)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
