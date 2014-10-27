from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest

from sports.views import home
from sports.models import Product


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_view_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class ProductModelTest(TestCase):

    def test_saving_and_retrieving_products(self):
        first_product = Product()
        first_product.name = 'Product 1'
        first_product.category = 'Category 1'
        first_product.description = 'Description 1'
        first_product.price = 100.00
        first_product.save()

        second_product = Product()
        second_product.name = 'Product 2'
        second_product.category = 'Category 2'
        second_product.description = 'Description 2'
        second_product.price = 200.00
        second_product.save()

        saved_products = Product.objects.all()
        self.assertEqual(saved_products.count(), 2)

        first_saved_product = saved_products[0]
        second_saved_product = saved_products[1]
        self.assertEqual(first_saved_product.name, 'Product 1')
        self.assertEqual(second_saved_product.name, 'Product 2')


class ProductsViewTest(TestCase):

    def test_displays_all_products(self):
        product1 = Product()
        product1.name = 'Product 1'
        product1.category = 'Category 1'
        product1.description = 'Description 1'
        product1.price = 100.00
        product1.save()

        product2 = Product()
        product2.name = 'Product 2'
        product2.category = 'Category 1'
        product2.description = 'Description 1'
        product2.price = 100.00
        product2.save()

        response = self.client.get('/')

        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')