from project.models import Post, Project
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Trunc
import json
from .filters_for_widgets import posts_agregator

def content_volume_top_10_source(request, pk):
  project = Project.objects.get(id=pk)
  posts = posts_agregator(project)
  body = json.loads(request.body)
  smpl_freq = body['smpl_freq']
  top_brands = list(map(lambda x: x['feedlink__source1'], list(posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:10])))
  results = [{source: list(posts.filter(feedlink__source1=source).annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date"))} for source in top_brands]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_brands[elem]])):
      dates.add(str(results[elem][top_brands[elem]][i]['date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_brands[elem]][i]['date']) for i in range(len(results[elem][top_brands[elem]]))})):
        for i in range(len(results[elem][top_brands[elem]])):
          if date == str(results[elem][top_brands[elem]][i]['date']): 
            list_dates.append({"date": date, "post_count": results[elem][top_brands[elem]][i]['created_count']})
      else:
        list_dates.append({"date": date, "post_count": 0})
    if (top_brands[elem] == '') or (top_brands[elem] == None) or ('img' in top_brands[elem]) or (top_brands[elem] == 'None') or (top_brands[elem] == 'null') or not top_brands[elem]:     
      res.append({'Missing in source': list_dates}) 
    else:
      res.append({top_brands[elem]: list_dates})    
  return JsonResponse(res, safe = False)
