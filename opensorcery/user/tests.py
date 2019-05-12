from django.test import TestCase

from .models import User


class UserTests(TestCase):

    def test_userpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        user = User()
        self.assertTrue(user)

    def test_user_username_attribute(self):
        user = User(user_name="lol")
        self.assertTrue(user.user_name)

    def test_user_email_attribute(self):
        user = User(email="lol")
        self.assertTrue(user.email)

    # test user doesnt have null values

    # test username min and max length

    # test user str representation

    # test user has certain attributes
