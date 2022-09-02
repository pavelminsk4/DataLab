from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  max_users = models.IntegerField()
  max_projects = models.IntegerField()
  max_online_feeds = models.IntegerField()
  max_social_feeds = models.IntegerField()
  max_twitter_data = models.IntegerField()

  def __str__(self):
    return self.name
  
class Workspace(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  members = models.ManyToManyField(User,null=True,blank=True)
  company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Project(models.Model):
  title = models.CharField(max_length=100)
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  note = models.CharField(max_length=200, null=True, blank=True)
  keywords = models.CharField(max_length=200, null=True, blank=True)
  ignore_keywords = models.CharField(max_length=200, null=True, blank=True)
  max_items = models.CharField(max_length=200, null=True, blank=True)
  image = models.ImageField(null=True, blank=True, upload_to='images')
  arabic_name = models.CharField(max_length=100, null=True, blank=True)
  english_name = models.CharField(max_length=100, null=True, blank=True)
  workspase = models.ForeignKey(Workspace, related_name='projects', blank=True, null=True, on_delete=models.CASCADE)
  social = models.BooleanField(default=False)
  online = models.BooleanField(default=False)
  premium = models.BooleanField(default=False)

  def __str__(self):
    return self.title
class Feedlinks(models.Model):

  category1 = (
          ('news', 'News'),
          ('magazine', 'Magazine'),
          ('blog', 'Blog'),
          ('forum', 'Forum'),
          )

  url = models.URLField(max_length=200,null=True,blank=True,unique=True)
  source = models.CharField("Source",max_length=200, null=True, blank=True)
  page = models.CharField("Page",max_length=200,null=True,blank=True)
  creator = models.IntegerField('Creator', default=1)
  creationdate = models.DateTimeField(auto_now_add=True)
  lastupdate = models.DateTimeField(auto_now=True)
  errornotes = models.CharField("Error Note",max_length=200,null=True,blank=True)
  nooffeeds = models.IntegerField(default=0)
  circle = models.IntegerField(default=0)
  country =  models.CharField("Country",max_length=200,null=True,blank=True)
  source1 = models.CharField("Source1",max_length=200,null=True,blank=True)
  boze = models.CharField("Boze",max_length=30,null=True,blank=True)
  myscript = models.CharField("Script",max_length=30,null=True,blank=True)
  status_code = models.IntegerField(default=0)
  linklanguage = models.CharField("Language",max_length=200,null=True,blank=True)
  languagecode = models.CharField("Language Code",max_length=2,null=True,blank=True)
  sourceurl = models.URLField(max_length=200,null=True,blank=True)
  issourcefeed = models.BooleanField(default=False)
  
  class Meta:
      indexes = [models.Index(fields=['url', ]), models.Index(fields=['errornotes', ])]

  def __str__(self):
    return self.url
