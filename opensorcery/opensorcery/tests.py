from django.test import TestCase


class OpensorceryTests(TestCase):

    def test_opensorcery_index_page_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_opensorcery_index_page_response_body(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, b"Welcome to Opensorcery")
