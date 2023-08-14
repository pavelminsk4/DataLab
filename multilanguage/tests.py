from common.factories.phrase_translations import PhraseTranslationsFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class MultilanguageTests(APITestCase):
    def setUp(self):
        PhraseTranslationsFactory(
            en='Translated English Text', ar='ترجمة نص إنجليزي')
        PhraseTranslationsFactory(
            en='Interface Element that does not have an Arabic translation, but is stored in the DB', ar=None)

    def test_response(self):
        url = reverse('multilanguage:multilanguage')

        data = {'en': 'Translated English Text'}
        response = self.client.post(url, data, format='json')
        res = {'ar': 'ترجمة نص إنجليزي'}
        self.assertEqual(json.loads(response.content), res)

        data = {'en': 'Interface Element that does not have an Arabic translation, but is stored in the DB'}
        response = self.client.post(url, data, format='json')
        res = {'ar': 'Interface Element that does not have an Arabic translation, but is stored in the DB'}
        self.assertEqual(json.loads(response.content), res)

        data = {'en': 'Random Text that requested for the first time'}
        response = self.client.post(url, data, format='json')
        res = {'ar': 'Random Text that requested for the first time'}
        self.assertEqual(json.loads(response.content), res)
