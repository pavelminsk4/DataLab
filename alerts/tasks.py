from celery import shared_task
from .models import Alert

import smtplib
from email.message import EmailMessage
from pathlib import Path
import os
import environ

from alerts.services.social_posts_agregator import social_posts_agregator
from alerts.services.online_posts_agregator import posts_agregator
from alerts.services.fill_social_part_of_sample import fill_social_part_of_sample
from alerts.services.fill_part_of_sample import fill_part_of_sample
from alerts.services.check_new_posts import check_new_posts

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

@shared_task
def alert_sender():
  alerts = Alert.objects.all()
  for alert in alerts:
    delta = check_new_posts(alert)
    if delta >= alert.triggered_on_every_n_new_posts:
      if alert.module_type == 'Project':
        posts = posts_agregator(alert.module_project_id).order_by('-creationdate')[:alert.how_many_posts_to_send]
      if alert.module_type == 'ProjectSocial':
        posts = social_posts_agregator(alert.module_project_id).order_by('-created_at')[:alert.how_many_posts_to_send]
      users = alert.user.all()
      mails_list = list(users.values_list('email', flat=True))

      msg = EmailMessage()
      msg['Subject'] = f'''Your '{alert.title}' alert from the '{alert.project.title}' Datalab project has been triggered.'''
      msg['From'] = 'Datalab'
      msg['To'] = mails_list

      part_of_smpl = ''''''
      for p in posts:
        if alert.module_type == 'Project':
          part_of_smpl += fill_part_of_sample(p)
        if alert.module_type == 'ProjectSocial':
          part_of_smpl += fill_social_part_of_sample(p)

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
