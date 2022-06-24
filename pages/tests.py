from django.test import TestCase
from django.urls import reverse


class TestPages(TestCase):

    def test_homepage_with_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_with_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_us_page_with_url(self):
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about_us.html')

    def test_about_us_page_with_url_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about_us.html')


