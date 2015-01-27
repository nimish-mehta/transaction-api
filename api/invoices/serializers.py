from django.forms import widgets
from rest_framework import serializers
from .models import Invoice, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction


class InvoiceSerializer(serializers.Serializer):
    class Meta:
        model = Invoice
        fields = ('id', 'customer', 'transactions')
