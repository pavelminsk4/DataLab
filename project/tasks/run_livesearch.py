from talkwalker.classes.livestream import Livestream
from api.services.rss_search_service import RssSearchService
from project.models import Project
from celery import shared_task


@shared_task
def run_talkwalker_livesearch():
    projects = Project.objects.filter(status=Project.STATUS_ACTIVE, sources__contains=['talkwalker'])

    for project in projects:
        Livestream(project.id, 'Project').read()


@shared_task
def reset_collectors():
    projects = Project.objects.filter(status=Project.STATUS_ACTIVE, sources__contains=['talkwalker'])

    for project in projects:
        stream = Livestream(project.id, 'Project')
        stream.delete()
        stream.create()
        project.resume_offset = 'earliest'
        project.save()


@shared_task
def run_rss_livesearch():
    projects = Project.objects.filter(status=Project.STATUS_ACTIVE, sources__contains=['rss'])

    for project in projects:
        RssSearchService().execute(project.id)
