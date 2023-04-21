from alerts.services.online_posts_agregator import posts_agregator
from alerts.services.social_posts_agregator import social_posts_agregator

def check_new_posts(item, triggered_on_every_n_new_posts):
  previous_posts_count = item.previous_posts_count
  if item.module_type == 'Project':
    total_posts_count = posts_agregator(item.module_project_id).count()
  if item.module_type == 'ProjectSocial':
    total_posts_count = social_posts_agregator(item.module_project_id).count()
  delta = total_posts_count - previous_posts_count
  if delta >= triggered_on_every_n_new_posts:
    item.previous_posts_count = total_posts_count
    item.save()
    return delta
  return False
