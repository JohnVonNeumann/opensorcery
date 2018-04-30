from django.test import TestCase

# Create your tests here.
class UserTests(TestCase):

    def test_user_page_after_direct_uri(self):
        response = self.client.get('/user')
        self.assertEqual(response.status_code, 301)

    # tests need to be included for the results of a successful auth, along with tests that correctly reference the location of the unauthed redirect
