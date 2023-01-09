from celery import shared_task
from .models import Alert
from project.models import Project, Post
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

def check_new_posts(alert):
  triger_on_every_new_posts = alert.triggered_on_every_n_new_posts
  previous_posts_count = alert.privious_posts_count
  total_posts_count = posts_agregator(alert.project).count()
  delta = total_posts_count - previous_posts_count
  if delta >= triger_on_every_new_posts:
    alert.privious_posts_count = total_posts_count
    alert.save()
    return delta
  return False

def fill_part_of_sample(p):
  return f'''
    <section class="email-post-wrapper">
      <div class="email-post-date">{str(p.entry_published.ctime())}</div>
      <h2 class="email-post-title">
        {p.entry_title}
      </h2>
      <p class="email-post-content">
        {p.entry_summary}
      </p>
      <div class="email-post-info">
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/language.png" />
          <span>Language: {p.feed_language.language}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/sentiment.png" />
          <span>Sentiment: {p.sentiment}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/source.png" />
          <span>Source: {p.feedlink.source1}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/location.png" />
          <span>Source country: {p.feedlink.country}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/global-rank.png" />
          <span>Global Rank: {p.feedlink.alexaglobalrank}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/calendar.png" />
          <span>Date: {str(p.entry_published.ctime())}</span>
        </div>
      </div>
      <a href="{p.entry_link}" class="email-post-button">
        View Post
      </a>
    </section>
  '''

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
      msg['Subject'] = f'''Your '{alert.title}' alert from the '{alert.project.title}' Datalab project has been triggered.'''
      msg['From'] = 'Datalab'
      msg['To'] = mails_list

      part_of_smpl = ''''''
      for p in posts:
        part_of_smpl = part_of_smpl + fill_part_of_sample(p)

      styles = '''
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
        .email-wrapper {
          width: 100%;
          padding: 15px 10px 20px;
          background-color: #F0F2F5;
          font-family: 'Poppins', sans-serif;
        }
        .email-datalab-logo {
          display: block;
          margin: 0 auto 20px;
        }
        .email-post-wrapper {
          max-width: 580px;
          padding: 16px 12px 28px;
          margin: 0px auto 20px;
          background-color: #ffffff;
          border-radius: 8px;
        }
        .email-post-date {
          margin-bottom: 5px;
          font-size: 14px;
          color:#5C6E80;
        }
        .email-post-title {
          margin: 0;
          font-size: 18px;
          color: #29333D;
        }
        .email-post-content {
          margin: 12px 0 16px;
          font-size: 16px;
          color: #5C6E80;
        }
        .email-post-info {
          margin-bottom: 28px;
        }
        .email-post-info-item {
          display: flex;
          font-size: 12px;
          color:#5C6E80;
        }
        .email-post-info-item img {
          margin-right: 6px;
        }
        .email-post-button {
          display: block;
          padding: 10px;
          background-color: #055FFC;
          border-radius: 8px;
          text-align: center;
          font-size: 14px;
          font-weight: 500;
          text-decoration: none;
          color: #ffffff !important;
        }
        .email-links-wrapper {
          display: flex;
          width: fit-content;
          margin: 0 auto;
        }
        .email-link {
          color: #5C6E80;
        }
        .divider {
          margin: 0 10px;
          border: 0.5px solid #FFFFFF;
        }
      '''
      smpl = f'''
      <!DOCTYPE html>
      <html>
      <head>
        <style type="text/css">
          {styles}
        </style>
      </head>
      <body>
        <div class="email-wrapper">
          <img class="email-datalab-logo" src="{env('APP_URL')}/static/email_alerts_icons/datalab-logo-01.png" />
          {part_of_smpl}
          <div class="email-links-wrapper">
            <a href="{env('APP_URL')}" class="email-link">
              GO TO WEBSITE
            </a>
          </div>
        </div>
      </body>
      </html>
      '''
      msg.set_content(smpl, subtype='html')

      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(env('EMAIL_HOST_USER'), env('EMAIL_HOST_PASSWORD'))
        smtp.send_message(msg)
