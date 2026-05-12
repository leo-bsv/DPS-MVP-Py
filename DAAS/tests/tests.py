from django.test import TestCase
from django.urls import reverse

class MyViewTests(TestCase):
    def test_get_page(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')