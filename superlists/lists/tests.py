from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from lists.views import home_page


class SmokeTest(TestCase):

    def test_root_url_resolves_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)