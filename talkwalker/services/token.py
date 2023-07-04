from pathlib import Path
import requests
import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


def get_token():
    token = env('TALKWALKER_TOKEN')
    return token
