from django.test import TestCase


class IndexTestCase(TestCase):

    def test_i18n(self):
        response = self.client.get('/test-parking/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.LANGUAGE_CODE, 'en')

        response = self.client.get('/de/test-parking/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.LANGUAGE_CODE, 'de')

        response = self.client.get('/pl/test-parking/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.LANGUAGE_CODE, 'pl')

        response = self.client.get('/de/pl/test-parking/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.wsgi_request.LANGUAGE_CODE, 'de')

        response = self.client.get('/pl/de/test-parking/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.wsgi_request.LANGUAGE_CODE, 'pl')
