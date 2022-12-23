from rest_framework.test import APITestCase
from rest_framework import status
from widgets.models import Dimensions
from django.urls import reverse
import json

class DimensionsTests(APITestCase):
  def create_dimensions(self):
    Dimensions.objects.create(title='Content Author')
    Dimensions.objects.create(title='Content Country')
    Dimensions.objects.create(title='Content Language')

  def test_dimensions_api(self):
    self.create_dimensions()
    url = reverse('dimensions-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        'id':1,
        'title':'Content Author',
        'description':'',
      },
      {
        'id':2,
        'title':'Content Country',
        'description':'',
      },
      {
        'id':3,
        'title':'Content Language',
        'description':'',
      },
    ]
    self.assertEqual(json.loads(response.content), res)
    url2 = reverse('dimensions-detail', kwargs={'pk':3})
    self.client.delete(url2)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        'id':1,
        'title':'Content Author',
        'description':'',
      },
      {
        'id':2,
        'title':'Content Country',
        'description':'',
      },
    ]
    self.assertEqual(json.loads(response.content), res)
    url3 = reverse('dimensions-detail', kwargs={'pk':2})
    data = { 'id':2, 'title':'Content City'}
    self.client.patch(url3, data)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        'id':1,
        'title':'Content Author',
        'description':'',
      },
      {
        'id':2,
        'title':'Content City',
        'description':'',
      },
    ]
    self.assertEqual(json.loads(response.content), res)
