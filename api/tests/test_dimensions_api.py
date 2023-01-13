from rest_framework.test import APITestCase
from rest_framework import status
from widgets.models import Dimensions
from django.urls import reverse
import json

class DimensionsTests(APITestCase):
  def test_dimensions_api(self):
    dim1 = Dimensions.objects.create(title='Content Author')
    dim2 = Dimensions.objects.create(title='Content Country')
    dim3 = Dimensions.objects.create(title='Content Language')
    url = reverse('dimensions-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        'id':dim1.id,
        'title':'Content Author',
        'description':'',
      },
      {
        'id':dim2.id,
        'title':'Content Country',
        'description':'',
      },
      {
        'id':dim3.id,
        'title':'Content Language',
        'description':'',
      },
    ]
    self.assertEqual(json.loads(response.content), res)
    url2 = reverse('dimensions-detail', kwargs={'pk':dim3.id})
    self.client.delete(url2)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        'id':dim1.id,
        'title':'Content Author',
        'description':'',
      },
      {
        'id':dim2.id,
        'title':'Content Country',
        'description':'',
      },
    ]
    self.assertEqual(json.loads(response.content), res)
    url3 = reverse('dimensions-detail', kwargs={'pk':dim2.id})
    data = { 'id':dim2.id, 'title':'Content City'}
    self.client.patch(url3, data)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        'id':dim1.id,
        'title':'Content Author',
        'description':'',
      },
      {
        'id':dim2.id,
        'title':'Content City',
        'description':'',
      },
    ]
    self.assertEqual(json.loads(response.content), res)
