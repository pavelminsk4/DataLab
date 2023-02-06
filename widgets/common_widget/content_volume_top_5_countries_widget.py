from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Trunc
import json
from .filters_for_widgets import post_agregator_with_dimensions

def content_volume_top_5_countries(request, pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  body = json.loads(request.body)
  smpl_freq = body['smpl_freq']
  top_countries = list(map(lambda x: x['feedlink__country'], list(posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:5])))
  results = [{country: list(posts.filter(feedlink__country=country).annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date"))} for country in top_countries]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_countries[elem]])):
      dates.add(str(results[elem][top_countries[elem]][i]['date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_countries[elem]][i]['date']) for i in range(len(results[elem][top_countries[elem]]))})):
        for i in range(len(results[elem][top_countries[elem]])):
          if date == str(results[elem][top_countries[elem]][i]['date']): 
            list_dates.append({"date": date, "post_count": results[elem][top_countries[elem]][i]['created_count']})
      else:
        list_dates.append({"date": date, "post_count": 0})
    if (top_countries[elem] == '') or (top_countries[elem] == None) or ('img' in top_countries[elem]) or (top_countries[elem] == 'None') or (top_countries[elem] == 'null') or not top_countries[elem]:    
      res.append({'Missing in source': list_dates}) 
    else:
      res.append({top_countries[elem]: list_dates})    
  return JsonResponse(res, safe = False)
