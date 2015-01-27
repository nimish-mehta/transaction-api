from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice, Transaction


# Create your tests here.
class InvoiceModelTestCase(TestCase):

    def test_save(self):
        name = "test"
        inv = Invoice(customer=name)
        inv.save()
        self.assertEqual(inv.customer, name)

    def test_default_price(self):
        name = "test"
        inv = Invoice(customer=name)
        inv.save()
        self.assertEqual(inv.total_amount, 0)

    def test_default_quantity(self):
        name = "test"
        inv = Invoice(customer=name)
        inv.save()
        self.assertEqual(inv.total_quantity, 0)

    def test_transaction_quantity_update(self):
        product = "testProd"
        quantity = 2
        price = 3.14
        customer_name = "test"
        inv = Invoice(customer=customer_name)
        inv.save()
        transaction = Transaction(product=product, quantity=quantity,
                                  price=price, invoice=inv)
        transaction.save()
        inv.save()
        self.assertEqual(inv.total_quantity, quantity)

    def test_multiple_transaction_update(self):
        product = "testProd"
        quantity = 2
        price = 3.14
        customer_name = "test"
        inv = Invoice(customer=customer_name)
        inv.save()
        transaction = Transaction(product=product, quantity=quantity,
                                  price=price, invoice=inv)
        transaction.save()
        transaction = Transaction(product=product, quantity=quantity,
                                  price=price, invoice=inv)
        transaction.save()
        inv.save()
        self.assertEqual(inv.total_quantity, quantity*2)


class TransactionModelTestCase(TestCase):

    def test_save(self):
        product = "testProd"
        quantity = 2
        price = 3.14
        customer_name = "test"
        inv = Invoice(customer=customer_name)
        inv.save()
        transaction = Transaction(product=product, quantity=quantity,
                                  price=price, invoice=inv)
        transaction.save()
        self.assertEqual(transaction.product, product)

    def test_total(self):
        product = "testProd"
        quantity = 2
        price = 3.14
        customer_name = "test"
        inv = Invoice(customer=customer_name)
        inv.save()
        transaction = Transaction(product=product, quantity=quantity,
                                  price=price, invoice=inv)
        transaction.save()
        self.assertEqual(transaction.total, price * quantity)


class APITest(TestCase):
    message = {
        "customer": "Name",
        "transactions": [
            {
                "product": "prod",
                "quantity": 2,
                "price": 3
            }
        ]
    }
    url = "/invoice/"
    def test_post(self):
        client = APIClient()
        post_response = client.post(self.url, self.message, format='json')
        self.assertEqual(post_response.data.get("id"), 1)
        self.assertEqual(post_response.data.get("total_amount"), "6.00")
