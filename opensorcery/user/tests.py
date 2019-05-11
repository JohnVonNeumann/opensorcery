from django.test import TestCase

from .models import User

# Create your tests here.
class UserTests(TestCase):

    def test_userpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        user = User()
        self.assertTrue(user)
