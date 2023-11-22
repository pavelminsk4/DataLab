from project.models import Project
from alerts.services.online_posts_aggregator import posts_aggregator
from django.utils import timezone


class RssSearchService:
    def execute(self, id):
        project = Project.objects.filter(id=id).first()

        if project is None or project.status != Project.STATUS_ACTIVE or project.synched_at is None:
            return

        ends_at = timezone.now()

        for post in posts_aggregator(project.id, project.synched_at, ends_at):
            project.posts.add(post)

        project.synched_at = ends_at
        project.save()
