from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from .models import Logs
from .utils import check_status_len

# Create your tests here.

class LogsTestCase(APITestCase):

    # fixtures to store test data
    fixtures = ('fixtures/test_data',)

    client = APIClient()

    def setUp(self):
        """
        load test data from fixtures
        """
        # Logs.objects.get(pk=1)

    def test_get_log_data_with_valid_data(self):
        """
        Getting data by calling logs api
        :return:
        """
        response = self.client.get("/api/logs/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[0]['title'], 'Tittle')

    def test_get_log_data_with_valid_id(self):
        """
        Getting data by calling logs api with id
        :return:
        """
        response = self.client.get("/api/logs/2/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 2)
        self.assertEqual(response.data['title'], 'Tittle2')

    def test_get_log_data_with_query_param(self):
        """
        Getting data by calling logs api with query params
        :return:
        """
        response = self.client.get("/api/logs/?title=Tittle")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[0]['status'], 200)

    def test_create_logs(self):
        """
        To create logs with post request
        :return:
        """
        test_data = {
                "title": "Test Title",
                "description": "This is test description",
                "status": 200,
                "content": "Test Content",
                "source": "nginx"
        }

        response = self.client.post("/api/logs/", data=test_data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.data['content'], 'Test Content')
        self.assertEqual(response.data['description'], 'This is test description')

    def test_check_status_len(self):
        result = check_status_len(200)
        self.assertEqual(True, result)

    def test_check_status_invalid(self):
        result = check_status_len(2000)
        self.assertEqual(False, result)



