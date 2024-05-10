import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):
    def test_create_product(self):
        """
        새로운 제품을 생성하고 응답을 검증합니다.
        """
        url = reverse('product_list')
        data = {'name': 'Test Product','description': "good" ,'price': 20 , 'in_stock':True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_get_product(self):
        """
        제품 목록을 가져오고 결과를 검증합니다.
        """
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_product(self,pk):
        product =  Product.objects.create(name='Test Produect', price=30)
        url = reverse('product_detail',args=[product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
        
class ProductRetrieveTests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Produect', price=20)
        self.url = reverse('product_detail',args=[self.product.id])
    
    def test_retrieve_produect(self):
        response = self.clientget(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response_data = json.loads(response.content.decode('utf-8'))  # 바이트 문자열을 디코딩하여 JSON으로 변환
        self.assertEqual(response_data['name'], 'Test Product') 