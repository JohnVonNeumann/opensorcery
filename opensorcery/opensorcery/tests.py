from django.test import TestCase

class OpensorceryTests(TestCase):

    def test_opensorcery_index_page_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print(response)

    def test_opensorcery_index_page_response_body(self):
        response = self.client.get('/')
        self.assertEqual(response.content, b"Welcome to Opensorcery")
