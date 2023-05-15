import json
import requests
from pathlib import Path
import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

def whatsappp_sender(phone_number, message_content):
    access_token = env('WHATSAPP_ACCESS_TOKEN')
    phone_number_id = env('WHATSAPP_PHONE_NUMBER_ID')
    recipient_phone_number = phone_number

    url = f"https://graph.facebook.com/v13.0/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }

    msg_body_params = [
        {
            "type": "text",
            "text": message_content
        }
    ]

    data = {
        'messaging_product': 'whatsapp',
        'to': recipient_phone_number,
        'type': 'template',
        'template': {
            'name': 'twenty_four_seven',
            'language': {
                'code': 'en_US'
            },
            'components': [
                {
                    'type': 'body',
                    'parameters': msg_body_params
                }

            ]
        }
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data)
    )

    if response.ok:
        return { 'status': 'Message sent'}
    else:
        return { 'status': 'Message not sent'}
