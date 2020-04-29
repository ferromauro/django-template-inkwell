from django.test import TestCase
# Test Various Path 

class UrlsTestCase(TestCase):
    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detail_status_code(self):
        response = self.client.get('/detail/1')
        self.assertEqual(response.status_code, 200)

    def test_create_status_code(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_list_status_code(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)