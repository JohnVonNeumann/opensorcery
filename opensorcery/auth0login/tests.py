from django.test import TestCase, override_settings

from auth0login.auth0backend import Auth0
# Create your tests here.

@override_settings(SOCIAL_AUTH_AUTH0_DOMAIN='test')
class Auth0BackendTestCase(TestCase):
    
    def test_authorization_url(self):
        client = Auth0()
        url = client.authorization_url()
        self.assertEqual(url, "https://test/authorize")

    def test_access_token_url(self):
        client = Auth0()
        url = client.access_token_url()
        self.assertEqual(url, "https://test/oauth/token")
