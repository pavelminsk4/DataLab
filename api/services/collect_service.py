from project.models import Project
from talkwalker.classes.livestream import Livestream
from talkwalker.classes.asker import Asker
from alerts.services.online_posts_aggregator import posts_aggregator
from django.utils import timezone
import environ

env = environ.Env()
ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]


class CollectService:
    id = None
    project = None

    def execute(self, id):
        self.id = id
        self.project = Project.objects.filter(id=id).first()

        if self.project is None:
            return

        [getattr(self, x)() for x in self.project.sources]

        self.project.status = Project.STATUS_ACTIVE
        self.project.synched_at = timezone.now()
        self.project.save()

    def talkwalker(self):
        if ALLOWED_HOSTS[0] == 'localhost':
            return

        Asker(self.id, 'Project').run()
        Livestream(self.id, 'Project').create()

    def rss(self):
        for post in posts_aggregator(self.id):
            self.project.posts.add(post)
