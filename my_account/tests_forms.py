from django.test import TestCase
from .forms import UserDetailsForm


class TestUserDetailsForm(TestCase):
    def test_user_details_form_is_valid(self):
        updated_user = UserDetailsForm({
          'user_first_name': 'testname',
          'user_last_name': 'testlastname',
          'user_phone_number': '123',
          'user_street_address1': 'testad1',
          'user_street_address2': 'testad2',
          'user_city': 'New York',
          'user_postcode': '5555',
          'user_country': 'AU',
          'user_delivery_notes': 'test notes',
                  })
        self.assertTrue(updated_user.is_valid())
