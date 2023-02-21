from project.models import *
import feedparser
import socket
import ssl

socket.setdefaulttimeout(3)
ssl._create_default_https_context = ssl._create_unverified_context

nfls= NewFeedlinks.objects.all().order_by('-created_at')
for nf in nfls:
  try:
    f = feedparser.parse(nf.url)
    nf.sourceurl = f.feed.link
    nf.source1 = f.feed.title
    nf.save()
  except:
    print('Error')
