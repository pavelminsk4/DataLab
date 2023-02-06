from project.models import Project
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import Trunc
import json
from .filters_for_widgets import post_agregator_with_dimensions

def content_volume_top_5_authors(request, pk):
  project = Project.objects.get(id=pk)
  posts = post_agregator_with_dimensions(project)
  body = json.loads(request.body)
  smpl_freq = body['smpl_freq']
  top_authors = list(map(lambda x: x['entry_author'], list(posts.values('entry_author').annotate(author_count=Count('entry_author')).order_by('-author_count')[:5])))
  results = [{author: list(posts.filter(entry_author=author).annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date"))} for author in top_authors]
  dates = set()
  for elem in range(len(results)):
    for i in range(len(results[elem][top_authors[elem]])):
      dates.add(str(results[elem][top_authors[elem]][i]['date']))
  res = []
  for elem in range(len(results)):
    list_dates = []
    for date in sorted(list(dates)):
      if date in sorted(list({str(results[elem][top_authors[elem]][i]['date']) for i in range(len(results[elem][top_authors[elem]]))})):
        for i in range(len(results[elem][top_authors[elem]])):
          if date == str(results[elem][top_authors[elem]][i]['date']): 
            list_dates.append({"date": date, "post_count": results[elem][top_authors[elem]][i]['created_count']})
      else:
        list_dates.append({"date": date, "post_count": 0})
    if (top_authors[elem] == '') or (top_authors[elem] == None) or ('img' in top_authors[elem]) or (top_authors[elem] == 'None') or (top_authors[elem] == 'null') or not top_authors[elem]:    
      res.append({'Missing in source': list_dates})    
    else:
      res.append({top_authors[elem]: list_dates})   
  return JsonResponse(res, safe = False)
