from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from project.models import Post
from tweet_binder.models import TweetBinderPost
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.views import filter_with_constructor, data_range_posts
from celery import shared_task


class WorkspaceTwentyFourSeven(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    members = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='twenty_four_seven_workspaces')

    def __str__(self):
        return self.title


class ProjectTwentyFourSeven(models.Model):
    PROJECT_TYPE = [
        ('online', 'Online'),
        ('social', 'Social'),
    ]
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User,related_name='creator_tfs', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    ignore_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    additional_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    workspace = models.ForeignKey(WorkspaceTwentyFourSeven, related_name='tfs_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
    start_search_date = models.DateTimeField()
    end_search_date = models.DateTimeField()
    author_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    language_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    country_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    source_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    sentiment_filter = ArrayField(models.CharField(max_length=100), default=None, null=True, blank=True)
    members = models.ManyToManyField(User, related_name='projects_tfs', blank=True)
    author_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    language_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    country_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    source_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    sentiment_dimensions = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    project_type = models.CharField(max_length=10, choices=PROJECT_TYPE, default='Online')

    def __str__(self):
        return self.title


@shared_task
def attach_online_posts(id):
    instance = ProjectTwentyFourSeven.objects.get(id=id)
    posts = data_range_posts(instance.start_search_date, instance.end_search_date)
    body = {
        'keywords': instance.keywords,
        'exceptions': instance.ignore_keywords,
        'additions': instance.additional_keywords,
        'country': instance.country_filter,
        'language': instance.language_filter,
        'source': instance.source_filter,
        'author': instance.author_filter,
        'sentiment': instance.sentiment_filter,
        'country_dimensions': instance.country_dimensions,
        'language_dimensions': instance.language_dimensions,
        'source_dimensions': instance.source_dimensions,
        'author_dimensions': instance.author_dimensions,
        'sentiment_dimensions': instance.sentiment_dimensions,
    }
    posts = filter_with_constructor(body, posts)
    for post in posts:
        item = Item.objects.create(online_post=post)
        item.save()
        instance.tfs_project_items.add(item)


@receiver(post_save, sender=ProjectTwentyFourSeven)
def attach_items(sender, instance, created, **kwargs):
  if created:
    if instance.project_type == 'online':
        attach_online_posts.delay(instance.pk)


class Item(models.Model):
    STATUS_CHOICES = [
        ('Picking', 'Picking'),
        ('Summary', 'Summary'),
        ('Q&A Check', 'Q&A Check'),
        ('Publishing', 'Publishing'),
        ('Published', 'Published'),
        ('Irrelevant','Irrelevant'),
    ]

    online_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    social_post = models.ForeignKey(TweetBinderPost, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Picking')
    header = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    original_content = models.TextField(blank=True, null=True)
    in_work = models.BooleanField(default=False)
    is_back = models.BooleanField(default=False)
    project = models.ForeignKey(ProjectTwentyFourSeven, on_delete=models.CASCADE, related_name='tfs_project_items', blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_id', 'online_post'], name='twenty four seven online item uniqueness constraint'),
            models.UniqueConstraint(fields=['project_id', 'social_post'], name='twenty four seven social item uniqueness constraint')
        ]

    def __str__(self):
        return str(self.project)
