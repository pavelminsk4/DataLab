from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TranslatorTests(APITestCase):
    case_1 = {
        'data': {
            'target_lang': 'english',
            'text': 'Очень длинный текст.',
        },
        'res': {
            'translated_text': 'Very long text.',
        },
    }

    case_2 = {
        'data': {
            'target_lang': 'arabic',
            'text': 'dog',
        },
        'res': {
            'translated_text': 'كلب',
        },
    }

    cases = [case_1, case_2]

    def test_translator_endpoint(self):
        for case in self.cases:
            url = reverse('twenty_four_seven:translator')
            response = self.client.post(url, case['data'], format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(json.loads(response.content), case['res'])
