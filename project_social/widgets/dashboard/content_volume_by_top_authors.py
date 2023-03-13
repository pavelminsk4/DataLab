from project_social.models import SocialWidgetDescription
from project_social.widgets.filters_for_widgets import *
from project_social.models import ProjectSocial
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.db.models import Count

def post_agregator_content_volume_top_authors(posts, aggregation_period, top_counts):
  top_authors = list(map(lambda x: x['user_name'], list(posts.values('user_name').annotate(authors_count=Count('user_name')).order_by('-authors_count')[:top_counts])))
  results = [{name: list(posts.filter(user_name=name).annotate(date=Trunc('creation_date', aggregation_period)).values("creation_date").annotate(created_count=Count('id')).order_by("date"))} for name in top_authors]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_authors[elem]])):
      dates.add(str(results[elem][top_authors[elem]][i]['creation_date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_authors[elem]][i]['creation_date']) for i in range(len(results[elem][top_authors[elem]]))})):
        for i in range(len(results[elem][top_authors[elem]])):
          if date == str(results[elem][top_authors[elem]][i]['creation_date']):
            list_dates.append({"creation_date": date, "post_count": results[elem][top_authors[elem]][i]['created_count']})
      else:
        list_dates.append({"creation_date": date, "post_count": 0})
    res.append({top_authors[elem]: list_dates})
  return res

def content_volume_by_top_authors(request, pk, widget_pk):
  project = ProjectSocial.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  widget = SocialWidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  res = post_agregator_content_volume_top_authors(posts, widget.aggregation_period, widget.top_counts)
  return JsonResponse(res, safe = False)
