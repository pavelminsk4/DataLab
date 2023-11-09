from talkwalker.classes.livestream import Livestream
from django_celery_beat.models import PeriodicTask


def stop_livestream(id):
    task = PeriodicTask.objects.get(name=f'LiveSearch_project_{id}')
    task.enabled = False
    task.save()
    ls = Livestream(id, 'Project')
    ls._Livestream__04_delete_collector()
    ls._Livestream__05_delete_stream()
