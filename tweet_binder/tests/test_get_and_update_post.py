from tweet_binder.models import add_post_to_database, TweetBinderPost
from tweet_binder.services.get_publications import get_publications
from django.test import TestCase
from django.conf import settings

import responses
import os
import re
import json


class TweetsTestCase(TestCase):
    def read_file(self, name):
        return '}\n{'.join(re.sub(r'\s+', '', open(os.path.join(settings.BASE_DIR, name)).read()).split('}{'))

    @responses.activate
    def test_get_publications(self):
        auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsidXNlciIsInR3aXR0ZXIiXSwiaXNBZG1pbiI6ZmFsc2UsIm5hbWUiOiJrcm9uc29mdCIsImVtYWlsIjoiYWhtZWQuc3VsaW1hbkBkYXRhbGFiLm5ldCIsImludGVyY29tIjp7InVzZXJIYXNoIjoiMmRiMGE0MjFjNmEwMjVmMjZjNmVkOTJhN2M4ZmQyYzRiYmJkODUxYjBiYTZmZTkzZGJiMmQzNDMwNmEyNzNmMyJ9LCJwcm9maWxlcyI6eyJ0d2l0dGVyIjp7ImlkIjoidW5kZWZpbmVkIiwiYWNjb3VudCI6eyJpZF9zdHIiOiJ1bmRlZmluZWQiLCJuYW1lIjoiVHdlZXQgQ2F0ZWdvcnkgRGF0YSIsInNjcmVlbl9uYW1lIjoia3JvbnNvZnQtdGVzdCIsInByb2ZpbGVfaW1hZ2VfdXJsIjoiaHR0cDovL3Bicy50d2ltZy5jb20vcHJvZmlsZV9pbWFnZXMvMjk2MzM0MjU2OS9lMzkyYmI2NzRkNjliOTNiY2FkNzhiYzgxMjhmNWRjMV9ub3JtYWwuanBlZyIsInByb2ZpbGVfaW1hZ2VfdXJsX2h0dHBzIjoiaHR0cHM6Ly9wYnMudHdpbWcuY29tL3Byb2ZpbGVfaW1hZ2VzLzI5NjMzNDI1NjkvZTM5MmJiNjc0ZDY5YjkzYmNhZDc4YmM4MTI4ZjVkYzFfbm9ybWFsLmpwZWciLCJsb2NhdGlvbiI6IldoZXJlIGEgVHdlZXQgaXMgVHdlZXRlZCIsImZvbGxvd2Vyc19jb3VudCI6MTczLCJlbWFpbCI6ImNhdGVnLm9yeXR3ZWV0c0BnbWFpbC5jb20ifX19LCJpYXQiOjE3MDE2NzQ5NzEsImV4cCI6MTcwNDI2Njk3MSwiYXVkIjoidXNlciIsInN1YiI6IjcxMjk3YzZlLTIxZGUtNDE0Ni1iZDhlLWFjNmQyYjc1ZGY3NyJ9.LMcnLHa39QH6LtpixrwSlkY_Rb1H5qZaNhs9I7xv0A8'
       
        responses.add(
            responses.GET,
            'https://api2.tweetbinder.com/reports/2b56b10d-411e-4704-a044-d7bd31cd741d/output',
            body=self.read_file('fixtures/tweet_binder/basic_search_1.json')
        )

        result = get_publications('2b56b10d-411e-4704-a044-d7bd31cd741d', auth_token)
        tweets = json.loads(result)['data']
        self.assertTrue(result)
        self.assertEqual(len(tweets), 10)

        add_post_to_database(tweets)

        self.assertEqual(TweetBinderPost.objects.all().count(), 10)

        responses.add(
            responses.GET,
            'https://api2.tweetbinder.com/reports/2b56b10d-411e-4704-a044-d7bd31cd7415/output',
            body=self.read_file('fixtures/tweet_binder/basic_search_2.json')
        )

        result = get_publications('2b56b10d-411e-4704-a044-d7bd31cd7415', auth_token)
        tweets = json.loads(result)['data']
        self.assertTrue(result)
        self.assertEqual(len(tweets), 10)

        add_post_to_database(tweets)

        self.assertEqual(TweetBinderPost.objects.all().count(), 11)

        new_tweet = TweetBinderPost.objects.get(post_id='1731631950350385191')

        self.assertEqual(new_tweet.count_favorites, 10)
