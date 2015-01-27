from django.forms import widgets
from rest_framework import serializers
from .models import Invoice, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'product', 'quantity', 'price', 'total')

class InvoiceSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    class Meta:
        model = Invoice
