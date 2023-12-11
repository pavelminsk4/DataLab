from api.views.users import filter_with_constructor, data_range_posts_for_24
from django.contrib.postgres.fields import ArrayField
from project.models import Post
from tweet_binder.models import TweetBinderPost
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from celery import shared_task
from bs4 import BeautifulSoup
from django.db import models
import requests


class WorkspaceTwentyFourSeven(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    members = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='twenty_four_seven_workspaces')

    def __str__(self):
        return self.title


class WARecipient(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectTwentyFourSeven(models.Model):
    PROJECT_TYPE = [
        ('online', 'Online'),
        ('social', 'Social'),
    ]
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name='creator_tfs', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    ignore_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    additional_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    workspace = models.ForeignKey(WorkspaceTwentyFourSeven, related_name='tfs_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
    start_search_date = models.DateTimeField()
    end_search_date = models.DateTimeField()
    author_filter = models.CharField(max_length=100, default=None, null=True, blank=True)
    language_filter = models.CharField(max_length=100, default=None, null=True, blank=True)
    country_filter = models.CharField(max_length=100, default=None, null=True, blank=True)
    source_filter = models.CharField(max_length=100, default=None, null=True, blank=True)
    sentiment_filter = models.CharField(max_length=100, default=None, null=True, blank=True)
    members = models.ManyToManyField(User, related_name='projects_tfs', blank=True)
    author_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    language_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    country_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    source_dimensions = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    sentiment_dimensions = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    project_type = models.CharField(max_length=10, choices=PROJECT_TYPE, default='Online')
    expert_mode = models.BooleanField(default=False)
    wa_recipient = models.ManyToManyField(WARecipient, blank=True)

    def __str__(self):
        return self.title


@shared_task
def attach_online_posts(id):
    instance = ProjectTwentyFourSeven.objects.get(id=id)
    posts = data_range_posts_for_24(instance.start_search_date, instance.end_search_date)
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

    for post in filter_with_constructor(body, posts):
        Item.objects.create(post=post, project=instance)


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
        ('Irrelevant', 'Irrelevant'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    social_post = models.ForeignKey(TweetBinderPost, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Picking')
    header = models.CharField(default='', max_length=1000, blank=True, null=True)
    text = models.CharField(default='', max_length=10000, blank=True, null=True)
    original_content = models.TextField(blank=True, null=True)
    in_work = models.BooleanField(default=False)
    is_back = models.BooleanField(default=False)
    project = models.ForeignKey(ProjectTwentyFourSeven, on_delete=models.CASCADE, related_name='tfs_project_items', blank=True, null=True)
    linked_items = models.ManyToManyField(to='self', related_name='attached_items', symmetrical=False, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_id', 'post'], name='twenty four seven online item uniqueness constraint'),
            models.UniqueConstraint(fields=['project_id', 'social_post'], name='twenty four seven social item uniqueness constraint')
        ]

    def __str__(self):
        return str(self.project)


def find_tags(tags):
    result_tags = []
    for tag in tags:
        if tag.find('a') is None and tag.parent.name != 'a' and not tag.has_attr('class'):
            result_tags.append(tag.get_text().strip())
    return result_tags


@shared_task
def get_full_text(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    else:
        page = resp.text
        soup = BeautifulSoup(page, 'html.parser')
        p_tags = soup.find_all('p')
        p_tags_text = find_tags(p_tags)
        sentence_list = [sentence for sentence in p_tags_text if '\n' not in sentence]
        sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
        full_text = '\n'.join(sentence_list)
        return full_text
