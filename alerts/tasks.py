from celery import shared_task
from .models import Alert
from project.models import Project, Post
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from functools import reduce
from django.db.models import Q

import smtplib
from email.message import EmailMessage
from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

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
  delta = total_posts_count - previous_posts_count
  if delta >= triger_on_every_new_posts:
    alert.privious_posts_count = total_posts_count
    alert.save()
    return delta
  return False

def fill_part_of_sample(p):
  return f'''<div style="display: inline-block; float: left; gap: 20px">
            <div style="height: 1px; background-color: #666666"; margin-top: 20px; margin-bottom: 20px></div>
            <div style="color: #666666">{str(p.entry_published.ctime())}</div>
            <h1 style="color: #000000">{p.entry_title}</h1>
            <section style="color: #545454; font-size: 14px">
              {p.entry_summary}
            </section>
            <div style="color: #31b800; font-size: 16px"; margin-top: 20px; margin-bottom: 20px>{p.feedlink.source1} {p.feed_language.language}</div>
            <a href="{p.entry_link}">
              <button style="padding: 10px; width: 120px">View Post</button>
            </a>
            <div style="height: 1px; background-color: #666666"; margin-top: 20px; margin-bottom: 20px></div>
          </div>'''

@shared_task
def alert_sender():
  alerts = Alert.objects.all()
  for alert in alerts:
    delta = check_new_posts(alert)
    if delta >= alert.triggered_on_every_n_new_posts:
      posts = posts_agregator(alert.project).order_by('-creationdate')[:alert.how_many_posts_to_send]
      users = alert.user.all()
      mails_list = list(users.values_list('email', flat=True))

      msg = EmailMessage()
      msg['Subject'] = 'Subject: Allert from your Anova project.'
      msg['From'] = 'Datalab'
      msg['To'] = mails_list

      part_of_smpl = ''''''
      for p in posts:
        part_of_smpl = part_of_smpl + fill_part_of_sample(p)
      smpl = f'''
      <!DOCTYPE html>
      <html>
      <body style="background-color: #ffffff">
        {part_of_smpl}
      </body>
      </html>
      '''
      msg.set_content(smpl, subtype='html')

      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(env('EMAIL_HOST_USER'), env('EMAIL_HOST_PASSWORD'))
        smtp.send_message(msg)
