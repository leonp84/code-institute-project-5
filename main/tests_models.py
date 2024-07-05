from django.test import TestCase
from datetime import datetime
import uuid
from .models import CustomerMessage, NewsLetterSignup
from .models import DiscountCode


class TestCustomerMessageCreation(TestCase):
    def setUp(self):
        self.new_message = CustomerMessage(
            customer_name='test',
            customer_email='test@email.com',
            product_name='',
            product_ref='',
            customer_message='test message',
            date_sent=datetime.now()
        )
        self.new_message.save()

    def test_new_message_creation(self):
        self.assertEqual(self.new_message.customer_name, 'test')
        self.assertEqual(self.new_message.customer_email, 'test@email.com')
        self.assertEqual(self.new_message.customer_message, 'test message')
        self.assertIsNotNone(self.new_message.date_sent)


class TestNewsLetterSignupCreation(TestCase):
    def setUp(self):
        self.new_signup = NewsLetterSignup(
            customer_email='test',
            token=uuid.uuid4(),
            is_verified=True,
            sign_up_date=datetime.now()
        )
        self.new_signup.save()

    def test_new_signup_creation(self):
        self.assertEqual(self.new_signup.customer_email, 'test')
        self.assertIsNotNone(self.new_signup.token)
        self.assertEqual(self.new_signup.is_verified, True)
        self.assertIsNotNone(self.new_signup.sign_up_date)


class TestDiscountCodeCreation(TestCase):
    def setUp(self):
        self.new_discount_code = DiscountCode(
            discount_code='TESTCD',
            date_created=datetime.now()
        )
        self.new_discount_code.save()

    def test_new_discount_code_creation(self):
        self.assertEqual(self.new_discount_code.discount_code, 'TESTCD')
        self.assertIsNotNone(self.new_discount_code.date_created)
