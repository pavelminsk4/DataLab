from django.db import models
from accounts.models import department
from project.models import Project, Post
from django.contrib.auth.models import User
from functools import reduce
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models import Q

class Alert(models.Model):
  title = models.CharField(max_length=50)
  project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='alerts')
  user = models.ManyToManyField(User, blank=True, null=True)
  triggered_on_every_n_new_posts = models.IntegerField(default=1)
  how_many_posts_to_send = models.IntegerField(default=1)
  alert_condition = models.CharField(max_length=50, blank=True, null=True)
  privious_posts_count = models.PositiveBigIntegerField(default=0)

  def __str__(self):
    return self.title

def keywords_posts(keys, posts):
  posts = posts.filter(reduce(lambda x,y: x | y, [Q(entry_title__contains=key) for key in keys]))
  return posts

def exclude_keywords_posts(posts, exceptions):
  to_be_removed = []
  for post in posts:
    for word in exceptions:
      if word in post.entry_title:
        to_be_removed.append(post.id)
        break
  posts = posts.exclude(id__in=to_be_removed)
  return posts

def additional_keywords_posts(posts, additions):
  for word in additions:
    posts = posts.filter(entry_title__contains=word)
  return posts

def posts_agregator(project):
  project = get_object_or_404(Project, pk = project.pk)
  posts = Post.objects.all()
  posts = keywords_posts(project.keywords, posts)
  if project.additional_keywords!=[]:
    posts = additional_keywords_posts(posts, project.additional_keywords)
  if project.ignore_keywords!=[]:
    posts = exclude_keywords_posts(posts, project.ignore_keywords)
  if project.country_filter!=None:
    posts = posts.filter(feedlink__country=project.country_filter)
  if project.language_filter!=None:
    posts = posts.filter(feed_language__language=project.language_filter)
  if project.source_filter!=None:
    posts = posts.filter(feedlink__source1=project.source_filter)
  if project.author_filter!=None:
    posts = posts.filter(entry_author=project.author_filter)
  if project.sentiment_filter!=None:
    posts = posts.filter(sentiment=project.sentiment_filter) 
  return posts


@receiver(post_save, sender=Alert)
def define_initial_posts_count(sender, instance, created, **kwargs):
  if created:
    initial_posts_count = posts_agregator(instance.project).count()
    instance.privious_posts_count = initial_posts_count
    instance.save()
