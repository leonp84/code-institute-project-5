from django.test import TestCase
from django.urls import reverse
from django.test import Client
import json
from product.models import Product


class AllProductViewTest(TestCase):
    def test_all_products_view_status_code(self):
        response = self.client.get(reverse('all_products'))
        self.assertTemplateUsed(response, 'product/all_products.html')
        self.assertEqual(response.status_code, 200)


class BreitlingViewTest(TestCase):
    def test_breitling_view_status_code(self):
        response = self.client.get(reverse('breitling'))
        self.assertTemplateUsed(response, 'product/breitling.html')
        self.assertEqual(response.status_code, 200)


class TagHeuerViewTest(TestCase):
    def test_tag_heuer_view_status_code(self):
        response = self.client.get(reverse('tag_heuer'))
        self.assertTemplateUsed(response, 'product/tag_heuer.html')
        self.assertEqual(response.status_code, 200)


class OmegaViewTest(TestCase):
    def test_omega_view_status_code(self):
        response = self.client.get(reverse('omega'))
        self.assertTemplateUsed(response, 'product/omega.html')
        self.assertEqual(response.status_code, 200)


class TissotViewTest(TestCase):
    def test_tissot_view_status_code(self):
        response = self.client.get(reverse('tissot'))
        self.assertTemplateUsed(response, 'product/tissot.html')
        self.assertEqual(response.status_code, 200)


class SaleViewTest(TestCase):
    def test_sale_view_status_code(self):
        response = self.client.get(reverse('sale'))
        self.assertTemplateUsed(response, 'product/sale.html')
        self.assertEqual(response.status_code, 200)


class ProductDetailViewTest(TestCase):
    def setUp(self):
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

    def test_product_detail_view_status_code(self):
        self.client = Client()
        response = self.client.get(reverse('product_detail', args=[
                                                  self.new_product.id]))

        self.assertTemplateUsed(response, 'product/product_detail.html')
        test_line = b'test watch description'
        self.assertIn(test_line, response.content)
        self.assertEqual(response.status_code, 200)


class CustomerProductMessageViewTest(TestCase):
    def test_customer_product_message_view_status_code(self):
        client = Client()
        response = client.post('/product/customer_product_message/', {
                    'customer_name': 'testname',
                    'customer_email': 'test_user@email.com',
                    'product_name': '',
                    'product_ref': '',
                    'customer_message': 'test message',
                }, content_type="application/json")
        response_check = json.loads(response.content)
        self.assertEqual(response_check[
                                'message'], 'Customer Message Received')


class SearchViewTest(TestCase):
    def setUp(self):
        self.new_product = Product(
            watch_brand='BR',
            title='search test watch name',
            ref='A988FD23',
            desc='test-description',
            watch_gender='F',
            watch_case_size=44,
            watch_material='Gold',
            watch_dial_colour='Blue',
            discount_percentage=10,
            price=90,
            image='test_image.jpg')
        self.new_product.save()

    def test_search_view_status_code(self):
        self.client = Client()
        response = self.client.post(reverse('search'), data={
                                        'search-input': 'test-description'})
        self.assertTemplateUsed(response, 'product/search_results.html')
        test_line = b'search test watch name'
        self.assertIn(test_line, response.content)
        self.assertEqual(response.status_code, 200)


class AdvancedSearchViewTest(TestCase):
    def setUp(self):
        self.new_product = Product(
            watch_brand='BR',
            title='advanced_search test watch name',
            ref='A988FD23',
            desc='test-description',
            watch_gender='F',
            watch_case_size=44,
            watch_material='Gold',
            watch_dial_colour='Blue',
            discount_percentage=0,
            price=90,
            image='test_image.jpg')
        self.new_product.save()

    def test_advanced_search_view_status_code(self):
        self.client = Client()
        response = self.client.post(
          reverse('advanced_search'), data={'keyword': 'test-description',
                                            'brand': 'BR,',
                                            'gender': 'F,',
                                            'dial_color': 'Blue,',
                                            'min-price': 0,
                                            'max-price': 100,
                                            })
        self.assertTemplateUsed(response, 'product/search_results.html')
        test_line = b'advanced_search test watch name'
        self.assertIn(test_line, response.content)
        self.assertEqual(response.status_code, 200)
