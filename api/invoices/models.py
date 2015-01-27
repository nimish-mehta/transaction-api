from django.db import models


# Create your models here.
class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2)
    total_quantity = models.IntegerField()

    def get_transactions(self):
        transactions = Transaction.objects.filter(invoice=self)
        return transactions

    def calculate_total_amount(self):
        t_list = self.get_transactions()
        amount = 0.0
        for transaction in t_list:
            amount = amount + float(transaction.total)
        return amount

    def calculate_total_quantity(self):
        t_list = self.get_transactions()
        quantity = 0
        for transaction in t_list:
            quantity = quantity + float(transaction.quantity)
        return quantity

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.total_amount = 0.0
            self.total_quantity = 0
        else:
            self.total_quantity = self.calculate_total_quantity()
            self.total_amount = self.calculate_total_amount()
        return super(Invoice, self).save()


class Transaction(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    invoice = models.ForeignKey(Invoice, related_name='transactions')

    def save(self, *args, **kwargs):
        self.total = float(self.price) * int(self.quantity)
        return super(Transaction, self).save()
