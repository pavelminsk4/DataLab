import requests
import json

def login(email, password):
    url = "https://api2.tweetbinder.com/authorize/email/login"

    payload = json.dumps({
    "email": email,
    "password": password
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsidXNlciIsInR3aXR0ZXIiXSwiaXNBZG1pbiI6ZmFsc2UsIm5hbWUiOiJrcm9uc29mdCIsImVtYWlsIjoidnZrQGtyb25vbnNvZnQuY29tIiwiaW50ZXJjb20iOnsidXNlckhhc2giOiIyZGIwYTQyMWM2YTAyNWYyNmM2ZWQ5MmE3YzhmZDJjNGJiYmQ4NTFiMGJhNmZlOTNkYmIyZDM0MzA2YTI3M2YzIn0sInByb2ZpbGVzIjp7InR3aXR0ZXIiOnsiaWQiOiJ1bmRlZmluZWQiLCJhY2NvdW50Ijp7ImlkX3N0ciI6InVuZGVmaW5lZCIsIm5hbWUiOiJUd2VldCBDYXRlZ29yeSBEYXRhIiwic2NyZWVuX25hbWUiOiJrcm9uc29mdC10ZXN0IiwicHJvZmlsZV9pbWFnZV91cmwiOiJodHRwOi8vcGJzLnR3aW1nLmNvbS9wcm9maWxlX2ltYWdlcy8yOTYzMzQyNTY5L2UzOTJiYjY3NGQ2OWI5M2JjYWQ3OGJjODEyOGY1ZGMxX25vcm1hbC5qcGVnIiwicHJvZmlsZV9pbWFnZV91cmxfaHR0cHMiOiJodHRwczovL3Bicy50d2ltZy5jb20vcHJvZmlsZV9pbWFnZXMvMjk2MzM0MjU2OS9lMzkyYmI2NzRkNjliOTNiY2FkNzhiYzgxMjhmNWRjMV9ub3JtYWwuanBlZyIsImxvY2F0aW9uIjoiV2hlcmUgYSBUd2VldCBpcyBUd2VldGVkIiwiZm9sbG93ZXJzX2NvdW50IjoxNzMsImVtYWlsIjoiY2F0ZWcub3J5dHdlZXRzQGdtYWlsLmNvbSJ9fX0sImlhdCI6MTY3NTA3Nzg2NCwiZXhwIjoxNjc3NjY5ODY1LCJhdWQiOiJ1c2VyIiwic3ViIjoiNzEyOTdjNmUtMjFkZS00MTQ2LWJkOGUtYWM2ZDJiNzVkZjc3In0.3f4qD6gYp1ODOecbsghYHmTTTVbrLAplBESA1W8A51c'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text