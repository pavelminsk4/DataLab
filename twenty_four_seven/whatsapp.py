from whatsapp_api_client_python import API
from pathlib import Path
import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


def whatsappp_sender(phone_number, message_content):
    token = env('WHATSAPP_ACCESS_TOKEN')
    id = env('WHATSAPP_PHONE_NUMBER_ID')
    chat_id = f'{phone_number}@c.us'

    greenAPI = API.GreenApi(id, token)
    response = greenAPI.sending.sendMessage(chat_id, message_content)
    if response.data is None:
        return { 'status': 'Message not sent'}
    else:
        return { 'status': 'Message sent'}
