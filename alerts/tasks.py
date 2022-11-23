from celery import shared_task
from .models import Alert
from django.core.mail import send_mail

def post_agregator():
  return True

def check_new_posts(alert):
  return True
  # triger_on_every_new_posts = alert.triggered_on_every_n_new_posts
  # previous_posts_count = alert.privious_posts_count
  # total_posts_count = post_agregator()
  # if total_posts_count - previous_posts_count >= triger_on_every_new_posts:
  #   alert.privious_posts_count = total_posts_count
  #   return True
  # return False

@shared_task
def alert_sender():
  alerts = Alert.objects.all()
  for alert in alerts:
    #posts_to_send = alert.how_many_posts_to_send
    users = alert.user.all()
    if check_new_posts(alert):
      mails_list = list(users.values_list('email', flat=True))
      send_mail(
        'Subject: Allert from your Anova project.',
        'There are new posts corresponding to the parameters in your project.',
        'from@example.com',
        mails_list,
        fail_silently=False,
      )
