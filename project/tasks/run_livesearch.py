from talkwalker.classes.livestream import Livestream
from project.models import Project
from celery import shared_task


@shared_task
def run_livesearch():
    projects = Project.objects.filter(status=Project.STATUS_ACTIVE, sources__contains=['talkwalker'])

    for project in projects:
        Livestream(project.id, 'Project').read()
