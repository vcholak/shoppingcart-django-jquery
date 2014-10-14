from django.test import TestCase
from django.core.urlresolvers import resolve

from sports.views import home


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
