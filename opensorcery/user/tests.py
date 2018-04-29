from django.test import TestCase

# Create your tests here.
class UserTests(TestCase):

    def test_userpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
