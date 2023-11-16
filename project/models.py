from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from reports.models import Templates
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from ndarraydjango.fields import NDArrayField
import numpy as np

from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db.models.functions import Upper


class Workspace(models.Model):
    title       = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    department  = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='workspaces')
    members     = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Feedlinks(models.Model):
    url             = models.URLField(max_length=400, null=True, blank=True, unique=True)
    country         = models.CharField('Country', max_length=200, null=True, blank=True)
    source1         = models.CharField('Source1', max_length=200, null=True, blank=True)
    sourceurl       = models.URLField(max_length=200, null=True, blank=True)
    alexaglobalrank = models.BigIntegerField(default=0)

    def __str__(self):
        return self.url


class Speech(models.Model):
    language = models.CharField('language', max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        indexes = [
            GinIndex(
                OpClass(Upper('language'), name='gin_trgm_ops'),
                name='tlw_language_gin_index',
            )
        ]


class Post(models.Model):
    entry_title               = models.TextField('entry_title', null=True, blank=True)
    entry_links_href          = models.TextField('entry_links_href', null=True, blank=True)
    entry_summary             = models.TextField('Summary', null=True, blank=True)
    creationdate              = models.DateTimeField(auto_now_add=True, db_index=True)
    entry_published           = models.DateTimeField(blank=True, null=True)
    entry_media_thumbnail_url = models.TextField('entry_media_thumbnail_url', null=True, blank=True)
    entry_media_content_url   = models.TextField('entry_media_content_url', null=True, blank=True)
    entry_author              = models.TextField('author', null=True, blank=True)
    feed_title                = models.TextField('feed_title', null=True, blank=True)
    feed_image_href           = models.TextField('feed_image_href', null=True, blank=True)
    feed_image_link           = models.TextField('feed_image_link', null=True, blank=True)
    sentiment                 = models.CharField('sentiment', max_length=8, default='neutral')
    imp_sentiment             = models.CharField('imp_sentiment', max_length=10, default='neutral')
    usersentiment             = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    updatedsentiment          = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    is_sentiment              = models.BooleanField(default=False)
    summary_vector            = ArrayField(NDArrayField(shape=(384), dtype=np.float32), blank=True, default=list)
    full_text                 = models.TextField('full_text', null=True, blank=True)
    category                  = models.TextField('Category', null=True, blank=True, default=None)
    source_type               = models.TextField('source_type', null=True, blank=True, default=None)

    feedlink      = models.ForeignKey(Feedlinks, on_delete=models.CASCADE, related_name='feedlink_feedsin', verbose_name='Feed Link')
    feed_language = models.ForeignKey(Speech, related_name='speech', on_delete=models.CASCADE)

    def __str__(self):
        return self.entry_title

    class Meta:
        indexes = [
            models.Index(fields=['entry_published']),
            models.Index(fields=['feedlink']),
            models.Index(fields=['feed_language']),
            models.Index(fields=['sentiment']),

            GinIndex(
                name='entry_title_gin_index',
                fields=['entry_title'],
                opclasses=['gin_trgm_ops'],
            ),
            GinIndex(
                name='entry_author_gin_index',
                fields=['entry_author'],
                opclasses=['gin_trgm_ops'],
            ),
        ]


class Project(models.Model):
    STATUS_CHOICES = (
        ('collecting_data', 'Collecting'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    title                = models.CharField(max_length=100)
    note                 = models.CharField(max_length=200, null=True, blank=True)
    keywords             = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    ignore_keywords      = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    additional_keywords  = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    sources              = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    max_items            = models.CharField(max_length=200, null=True, blank=True)
    image                = models.ImageField(null=True, blank=True, upload_to='images')
    arabic_name          = models.CharField(max_length=100, null=True, blank=True)
    english_name         = models.CharField(max_length=100, null=True, blank=True)
    social               = models.BooleanField(default=False)
    online               = models.BooleanField(default=False)
    premium              = models.BooleanField(default=False)
    source               = models.CharField(max_length=100, null=True, blank=True, default='Online')
    start_date           = models.DateTimeField(blank=True, null=True)
    start_search_date    = models.DateTimeField(blank=True, null=True)
    end_search_date      = models.DateTimeField(blank=True, null=True)
    report_format        = models.CharField(max_length=3, default='pdf')
    report_table_content = models.BooleanField(default=True)
    report_widgets       = models.BooleanField(default=True)
    report_content       = models.BooleanField(default=True)
    report_language      = models.CharField(max_length=10, default='English')

    author_filter        = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    language_filter      = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    country_filter       = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    source_filter        = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    sentiment_filter     = ArrayField(models.CharField(max_length=50), blank=True, null=True)

    author_dimensions    = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    language_dimensions  = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    country_dimensions   = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    source_dimensions    = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    sentiment_dimensions = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    query_filter         = models.CharField(max_length=5000, blank=True, null=True)
    expert_mode          = models.BooleanField(default=False)
    status               = models.CharField(max_length=20, choices=STATUS_CHOICES, default='collecting_data', blank=True)
    created_at           = models.DateTimeField(auto_now_add=True)

    creator         = models.ForeignKey(User, related_name='creator', on_delete=models.SET_NULL, null=True)
    report_template = models.ForeignKey(Templates, related_name='template', on_delete=models.SET_NULL, null=True)
    workspace       = models.ForeignKey(Workspace, related_name='projects', blank=True, null=True, on_delete=models.CASCADE)
    members         = models.ManyToManyField(User, related_name='members', blank=True)
    posts           = models.ManyToManyField(Post, blank=True)

    def save(self, *args, **kwargs):
        total_projects_count = 0
        if self.workspace:
            for workspace in self.workspace.department.workspaces.all():
                total_projects_count += workspace.projects.all().count()
            if total_projects_count < self.workspace.department.max_projects:
                return super(Project, self).save(*args, **kwargs)
            raise ValidationError('Projects creation limit reached')

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Project)
def increase_cur_number_of_projects(sender, instance, created, **kwargs):
    if created:
        if instance.workspace:
            instance.workspace.department.current_number_of_projects += 1
            instance.workspace.department.save()


@receiver(post_save, sender=Workspace)
def increase_cur_number_of_projects_2(sender, instance, created, **kwargs):
    if created:
        instance.department.current_number_of_projects += 1
        instance.department.save()


@receiver(pre_delete, sender=Project)
def decrease_cur_number_of_projects(sender, instance, using, **kwargs):
    instance.workspace.department.current_number_of_projects -= 1
    instance.workspace.department.save()


class NewFeedlinks(models.Model):
    url         = models.URLField(max_length=400, null=True, blank=True, unique=True)
    source1     = models.CharField('Source1', max_length=200, null=True, blank=True)
    sourceurl   = models.URLField(max_length=200, null=True, blank=True)
    country     = models.CharField('Country', max_length=200, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.url}, {self.is_approved}'


class CrawlerKeyword(models.Model):
    word = models.CharField('Word', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word


class CrawlerOption(models.Model):
    TBM_CHOICES = (
        ('None', 'Regular search'),
        ('isch', 'Google Images API'),
        ('lcl', 'Google Local API'),
        ('vid', 'Google Videos API'),
        ('nws', 'Google News API'),
        ('shop', 'Google Shopping API'),
    )

    SAFE_CHOICES = (
        ('active', 'Filtering for adult content - Active'),
        ('off', 'Filtering for adult content - Off'),
    )

    location   = models.CharField(max_length=50, default='Saudi Arabia')
    tbm        = models.CharField(max_length=5, default='nws', choices=TBM_CHOICES)
    gl         = models.CharField(max_length=3, default='sa')
    safe       = models.CharField(max_length=10, default='active', choices=SAFE_CHOICES)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TempFeedLinks(models.Model):
    url = models.URLField(max_length=200, null=True, blank=True, unique=True)
    alexaglobalrank = models.BigIntegerField()


class Status(models.Model):
    progress = models.IntegerField()

    def __str__(self):
        return str(self.progress)


class ChangingOnlineSentiment(models.Model):
    sentiment   = models.CharField('sentiment', max_length=10)
    department  = models.ForeignKey('accounts.department', on_delete=models.CASCADE)

    post = models.ForeignKey('project.Post', on_delete=models.CASCADE)

    def ___str__(self):
        return self.sentiment
