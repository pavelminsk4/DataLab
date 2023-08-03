from talkwalker.classes.livestream import Livestream
from celery import shared_task


@shared_task
def livesearch_sender(project_id):
    Livestream(project_id).read()
