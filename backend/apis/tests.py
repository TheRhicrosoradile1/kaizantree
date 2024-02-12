from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import *

class ItemsAPITest(APITestCase):
    def test_create_item(self):
        response = self.client.post('http://127.0.0.1:8000/items/list', {'name': 'Test Object'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_filter_items(self):
        response = self.client.post('http://127.0.0.1:8000/items/filter/?start_time=2023-01-01&end_time=2025-12-31&category_id=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_item(self):
        response = self.client.delete('http://127.0.0.1:8000/items/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_user_unauthenticate(self):
        response = self.client.delete('http://127.0.0.1:8000/items/1')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)