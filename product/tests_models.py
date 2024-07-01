from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User


class TestProductCreation(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.new_product = Product(
            watch_brand='BR',
            title='test watch',
            ref='A988FD23',
            desc='test watch description',
            watch_gender='F',
            watch_case_size=44,
            watch_material='Gold',
            watch_dial_colour='Blue',
            discount_percentage=10,
            price=90,
            image='test_image.jpg')
        self.new_product.save()

    def test_new_product_creation(self):
        self.assertEqual(self.new_product.watch_brand, 'BR')
        self.assertEqual(self.new_product.title, 'test watch')
        self.assertEqual(self.new_product.ref, 'A988FD23')
        self.assertEqual(self.new_product.watch_gender, 'F')
        self.assertEqual(self.new_product.watch_case_size, 44)
        self.assertEqual(self.new_product.watch_material, 'Gold')
        self.assertEqual(self.new_product.watch_dial_colour, 'Blue')
        self.assertEqual(self.new_product.discount_percentage, 10)
        self.assertEqual(self.new_product.price, 90)
        self.assertEqual(self.new_product.pre_discount_price(), 100)
        self.assertIsNotNone(self.new_product.image)
