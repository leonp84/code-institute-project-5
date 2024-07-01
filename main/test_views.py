from django.test import TestCase
from django.urls import reverse
from .forms import NewsLetterSignupsForm
from datetime import datetime
from django.test import Client
import uuid
import json


class PrivacyPolicyViewTest(TestCase):
    def test_privacy_policy_view_status_code(self):
        response = self.client.get(reverse('privacy_policy'))
        self.assertTemplateUsed(response, 'main/privacy_policy.html')
        self.assertEqual(response.status_code, 200)


class TermsAndConditionsViewTest(TestCase):
    def test_terms_and_conditions_view_status_code(self):
        response = self.client.get(reverse('terms_and_conditions'))
        self.assertTemplateUsed(response, 'main/terms_and_conditions.html')
        self.assertEqual(response.status_code, 200)


class AboutViewTest(TestCase):
    def test_about_view_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertEqual(response.status_code, 200)


class ContactUsViewTest(TestCase):
    def test_contact_us_view_status_code(self):
        response = self.client.get(reverse('contact_us'))
        self.assertTemplateUsed(response, 'main/contact_us.html')
        self.assertEqual(response.status_code, 200)


class VerifyEmailViewTest(TestCase):
    def setUp(self):
        self.new_signup = NewsLetterSignupsForm({
                    'customer_email': 'test@email.com',
                    'token': uuid.uuid4(),
                    'is_verified': True,
                    'sign_up_date': datetime.now(),
                  })
        self.temp_user = self.new_signup.save()

    def test_newsletter_signup_verified_view_status_code(self):
        response = self.client.get(reverse('verify_email', args=[
                                                self.temp_user.token]))
        self.assertTemplateUsed(
                      response, 'main/newsletter_signup_verified.html')
        self.assertEqual(response.status_code, 200)


class NewsLetterSignUpViewTest(TestCase):
    def test_newsletter_signup_view_status_code(self):
        client = Client()
        response = client.post('/newsletter_signup/', {
                    'customer_email': 'test_user@email.com',
                    'token': uuid.uuid4(),
                    'is_verified': False})
        self.assertTemplateUsed(
                      response, 'main/newsletter_signup.html')
        self.assertEqual(response.status_code, 200)


class CheckDiscountCodeViewTest(TestCase):
    def test_check_discount_code_view_status_code(self):
        client = Client()
        data = {'code': '000000'}
        data_json = json.dumps(data)
        response = client.post('my_account/check_discount_code', data_json, content_type="application/json")
        print('RESPONSE')
        print(response)
        self.assertEqual(response.status_code, '406')
