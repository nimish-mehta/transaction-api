from .models import Invoice, Transaction
from .serializers import InvoiceSerializer
from rest_framework import generics, status
from django.db import transaction as transaction_control
from rest_framework.response import Response
from rest_framework.views import APIView


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
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save_invoice(self, data):
        print data
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



class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
