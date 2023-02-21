import geonamescache
from project.models import *

gc =geonamescache.GeonamesCache()
cities = gc.get_cities()
arr = []

for city in cities:
  if cities[str(city)]['countrycode'] == 'SA':
    for altername in cities[str(city)]['alternatenames']:
      arr.append(altername)
      CrawlerKeyword.objects.create(word=altername + ' news').save()
