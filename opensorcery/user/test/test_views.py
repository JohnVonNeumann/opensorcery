from django.test import TestCase

# Create your tests here.
class UserTests(TestCase):

    def test_login_page(self):
        response = self.client.get('/user/login')
        self.assertEqual(response.status_code, 200)

    def test_login_page_template(self):
        response = self.client.get('/user/login')
        self.assertTemplateUsed(response, 'login.html')

    def test_login_page_template_contents(self):
        response = self.client.get('/user/login')
        self.assertContains(response, b'Login page')

    def test_post_login_welcome_page(self):
        response = self.client.get('/user/welcome')
        self.assertEqual(response.status_code, 200)

    def test_post_login_welcome_template_rendered(self):
        response = self.client.get('/user/welcome')
        self.assertTemplateUsed(response, 'welcome.html')

    def test_post_login_template_contents(self):
        response = self.client.get('/user/welcome')
        self.assertContains(response, b'Welcome to the landing page.')
