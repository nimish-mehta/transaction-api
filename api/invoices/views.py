from .models import Invoice, Transaction
from .serializers import InvoiceSerializer
from rest_framework import generics, status
from django.db import transaction as transaction_control
from rest_framework.response import Response


class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        data = request.DATA
        transaction_list = data.get('transactions', [])
        transaction_save_list = []
        customer = data.get('customer')
        with transaction_control.atomic():
            invoice = Invoice(customer=customer)
            invoice.save()
            for transaction in transaction_list:
                product = transaction.get('product')
                quantity = transaction.get('quantity')
                price = transaction.get('price')
                transaction = Transaction(product=product, quantity=quantity,
                                          price=price, invoice=invoice)
                transaction.save()
            invoice.save()
        serialized_response = InvoiceSerializer(invoice)
        print(serialized_response.data)
        return Response(serialized_response.data, status.HTTP_201_CREATED)

class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializers_class = InvoiceSerializer
