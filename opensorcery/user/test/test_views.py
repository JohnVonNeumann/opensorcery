from django.test import TestCase
from django.urls import resolve

from user.views import welcome

# Create your tests here.
class UserTests(TestCase):

    def test_user_path_resolves_to_welcome(self):
        response = resolve('/user/')
        self.assertEqual(response.func, welcome)

    def test_directly_accessing_user_page_without_auth(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/auth0?next=/user/", fetch_redirect_response=False)

    # tests need to be included for the results of a successful auth, along with tests that correctly reference the location of the unauthed redirect


#    def test_logged_in_uses_correct_template(self):
#        login = self.client.login(username='testuser1', password='12345')
#        resp = self.client.get('/login/auth0/')
#        print(resp.context)
#        self.assertEqual(str(resp.context['auth0user']), 'testuser1')
#        self.assertEqual(resp.status_code, 200)
