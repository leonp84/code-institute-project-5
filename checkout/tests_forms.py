from django.test import TestCase
from datetime import datetime
from .forms import OrderForm


class TestOrderForm(TestCase):
    def test_order_form_is_valid(self):
        new_order = OrderForm({
            'order_number': '12345678',
            'date_ordered': datetime.now(),
            'first_name': 'ftest',
            'last_name': 'ltest',
            'email': 'test@email.com',
            'phone_number': '0800 555',
            'street_address1': 'addr 1',
            'street_address2': 'addr 2',
            'city': 'New York',
            'postcode': '5555',
            'country': 'AU',
            'delivery_notes': 'test notes',
            'order_total': 1000,
            'watch_care_plan': False,
            'grand_total': 1000,
            'stripe_pid': 'pi_12345',
                  })
        self.assertTrue(new_order.is_valid())
