from celery import shared_task
from .models import Alert
from project.models import Project, Post
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from functools import reduce
from django.db.models import Q

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

def data_range_posts(start_date, end_date):
  interval = [start_date, end_date]
  posts = Post.objects.filter(entry_published__range=interval)
  return posts

def posts_agregator(project):
  project = get_object_or_404(Project, pk = project.pk)
  posts = data_range_posts(project.start_search_date, project.end_search_date)
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

def check_new_posts(alert):
  triger_on_every_new_posts = alert.triggered_on_every_n_new_posts
  previous_posts_count = alert.privious_posts_count
  total_posts_count = len(posts_agregator(alert.project))
  if total_posts_count - previous_posts_count >= triger_on_every_new_posts:
    alert.privious_posts_count = total_posts_count
    alert.save()
    return True
  return False

@shared_task
def alert_sender():
  alerts = Alert.objects.all()
  for alert in alerts:
    if check_new_posts(alert):
      users = alert.user.all()
      mails_list = list(users.values_list('email', flat=True))
      send_mail(
        'Subject: Allert from your Anova project.',
        'There are new posts corresponding to the parameters in your project.',
        'from@example.com',
        mails_list,
        fail_silently=False,
      )
