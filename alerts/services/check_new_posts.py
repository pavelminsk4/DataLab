from alerts.services.online_posts_agregator import posts_agregator
from alerts.services.social_posts_agregator import social_posts_agregator

def check_new_posts(alert):
  triger_on_every_new_posts = alert.triggered_on_every_n_new_posts
  previous_posts_count = alert.privious_posts_count
  if alert.module_type == 'Project':
    total_posts_count = posts_agregator(alert.module_project_id).count()
  if alert.module_type == 'ProjectSocial':
    total_posts_count = social_posts_agregator(alert.module_project_id).count()
  delta = total_posts_count - previous_posts_count
  if delta >= triger_on_every_new_posts:
    alert.privious_posts_count = total_posts_count
    alert.save()
    return delta
  return False
