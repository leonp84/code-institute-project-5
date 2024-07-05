from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from product.models import Product
from .models import CheckoutSingleItem, Order


class TestCheckoutSingleItemCreation(TestCase):
    def setUp(self):
        self.checkout_item = CheckoutSingleItem(
            order_number='TESTorder123',
            product=Product.objects.filter(id=20).first(),
            product_name_text='test_pr_1',
            product_ref_text='test_ref_1',
            product_price=500,
            quantity=1,
        )
        self.checkout_item.save()

    def test_checkout_item_creation(self):
        self.assertEqual(self.checkout_item.order_number, 'TESTorder123')
        self.assertEqual(self.checkout_item.product, Product.objects.filter(
                                                                id=20).first())
        self.assertEqual(self.checkout_item.product_name_text, 'test_pr_1')
        self.assertEqual(self.checkout_item.product_ref_text, 'test_ref_1')
        self.assertEqual(self.checkout_item.product_price, 500)
        self.assertEqual(self.checkout_item.quantity, 1)


class TestOrderCreation(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.new_order = Order(
            user=self.user,
            order_number='123456',
            date_ordered=datetime.now(),
            first_name='ftest',
            last_name='ltest',
            email='test@email.com',
            phone_number='0800555',
            street_address1='testadr1',
            street_address2='testadr2',
            city='New York',
            postcode='5555',
            country='AU',
            delivery_notes='test notes',
            order_total=5000,
            watch_care_plan=False,
            grand_total=5000,
            stripe_pid='pi_12345test',
        )
        self.new_order.save()

    def test_new_order_creation(self):
        self.assertEqual(self.new_order.user, self.user)
        self.assertEqual(self.new_order.order_number, '123456')
        self.assertIsNotNone(self.new_order.date_ordered)
        self.assertEqual(self.new_order.first_name, 'ftest')
        self.assertEqual(self.new_order.last_name, 'ltest')
        self.assertEqual(self.new_order.email, 'test@email.com')
        self.assertEqual(self.new_order.phone_number, '0800555')
        self.assertEqual(self.new_order.street_address1, 'testadr1')
        self.assertEqual(self.new_order.street_address2, 'testadr2')
        self.assertEqual(self.new_order.city, 'New York')
        self.assertEqual(self.new_order.postcode, '5555')
        self.assertEqual(self.new_order.country, 'AU')
        self.assertEqual(self.new_order.delivery_notes, 'test notes')
        self.assertEqual(self.new_order.order_total, 5000)
        self.assertEqual(self.new_order.watch_care_plan, False)
        self.assertEqual(self.new_order.grand_total, 5000)
        self.assertEqual(self.new_order.stripe_pid, 'pi_12345test')
