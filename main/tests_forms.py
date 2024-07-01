from django.test import TestCase
from .forms import NewsLetterSignupsForm, CustomerMessageForm
from datetime import datetime
import uuid


class TestNewsLetterSignupsForm(TestCase):
    def test_newsletter_signup_form_is_valid(self):
        new_newsletter_signup = NewsLetterSignupsForm({
                    'customer_email': 'test@email.com',
                    'token': uuid.uuid4(),
                    'is_verified': True,
                    'sign_up_date': datetime.now(),
                  })
        self.assertTrue(new_newsletter_signup.is_valid())


class TestCustomerMessageForm(TestCase):
    def test_customer_message_form_is_valid(self):
        new_customer_message = CustomerMessageForm({
                    'customer_name': 'test',
                    'customer_email': 'test@email.com',
                    'product_name': None,
                    'product_ref': None,
                    'customer_message': 'test message',
                    'date_sent': datetime.now(),
                  })
        self.assertTrue(new_customer_message.is_valid())
