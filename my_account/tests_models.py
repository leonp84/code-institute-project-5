from django.test import TestCase
from .models import UserDetail
from django.contrib.auth.models import User


class TestUserDetailCreation(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="myUsername2",
            password="myPassword2",
            email="test2@test.com"
        )
        self.new_userdetail = UserDetail.objects.filter(user=self.user).first()
        self.new_userdetail.user_first_name = 'ftest'
        self.new_userdetail.user_last_name = 'ltest'
        self.new_userdetail.user_phone_number = '01235'
        self.new_userdetail.user_street_address1 = 'testadr1'
        self.new_userdetail.user_street_address2 = 'testadr2'
        self.new_userdetail.user_city = 'New York'
        self.new_userdetail.user_postcode = '5555'
        self.new_userdetail.user_country = 'AU'
        self.new_userdetail.user_delivery_notes = 'test_notes'
        self.new_userdetail.save()

    def test_new_userdetail_creation(self):
        self.assertEqual(self.new_userdetail.user, self.user)
        self.assertEqual(self.new_userdetail.user_first_name, 'ftest')
        self.assertEqual(self.new_userdetail.user_last_name, 'ltest')
        self.assertEqual(self.new_userdetail.user_phone_number, '01235')
        self.assertEqual(self.new_userdetail.user_street_address1, 'testadr1')
        self.assertEqual(self.new_userdetail.user_street_address2, 'testadr2')
        self.assertEqual(self.new_userdetail.user_city, 'New York')
        self.assertEqual(self.new_userdetail.user_postcode, '5555')
        self.assertEqual(self.new_userdetail.user_country, 'AU')
        self.assertEqual(self.new_userdetail.user_delivery_notes, 'test_notes')
        self.assertIsNotNone(self.new_userdetail.wish_list)
