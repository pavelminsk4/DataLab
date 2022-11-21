from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from reports.models import Templates

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
  description = models.CharField(max_length=1000, null=True, blank=True)
  members = models.ManyToManyField(User, blank=True)
  company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class Project(models.Model):
  title = models.CharField(max_length=100)
  creator = models.ForeignKey(User,related_name='creator', on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  note = models.CharField(max_length=200, null=True, blank=True)
  keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  ignore_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  additional_keywords = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  max_items = models.CharField(max_length=200, null=True, blank=True)
  image = models.ImageField(null=True, blank=True, upload_to='images')
  arabic_name = models.CharField(max_length=100, null=True, blank=True)
  english_name = models.CharField(max_length=100, null=True, blank=True)
  workspace = models.ForeignKey(Workspace, related_name='projects', blank=True, null=True, on_delete=models.CASCADE)
  social = models.BooleanField(default=False)
  online = models.BooleanField(default=False)
  premium = models.BooleanField(default=False)
  source = models.CharField(max_length=100, null=True, blank=True)
  members = models.ManyToManyField(User,related_name='members',blank=True)
  start_search_date = models.DateTimeField()
  end_search_date = models.DateTimeField()
  report_template = models.ForeignKey(Templates, related_name='template', on_delete=models.SET_NULL, null=True)
  report_format = models.CharField(max_length=3, default='pdf')
  report_table_content = models.BooleanField(default=True)
  report_widgets = models.BooleanField(default=True)
  report_content = models.BooleanField(default=True)
  report_language = models.CharField(max_length=10, default='English')
  author_filter = models.CharField(max_length=50, blank=True, null=True)
  language_filter = models.CharField(max_length=50, blank=True, null=True)
  country_filter = models.CharField(max_length=50, blank=True, null=True)
  source_filter = models.CharField(max_length=50, blank=True, null=True)
  sentiment_filter = models.CharField(max_length=10, blank=True, null=True)

  def __str__(self):
    return self.title

class Feedlinks(models.Model):
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

  def __str__(self):
    return self.url

class Speech(models.Model):
  language = models.CharField('language', max_length=50)

  def __str__(self):
    return self.language
    
class Post(models.Model):
  feedlink =  models.ForeignKey(Feedlinks,on_delete=models.CASCADE,related_name='feedlink_feedsin',verbose_name ='Feed Link')
  entry_title = models.TextField("entry_title",null=True,blank=True)
  entry_title_detail_type = models.TextField("entry_title_detail_type",null=True,blank=True)
  entry_title_detail_language = models.TextField("entry_title_detail_language",null=True,blank=True)
  entry_title_detail_base = models.TextField("entry_title_detail_base",null=True,blank=True)
  entry_title_detail_value = models.TextField("entry_title_detail_value",null=True,blank=True)
  entry_links_rel = models.TextField("entry_links_rel",null=True,blank=True)
  entry_links_type = models.TextField("entry_links_type",null=True,blank=True)
  entry_links_href = models.TextField("entry_links_href",null=True,blank=True)
  entry_link = models.TextField("Link",null=True,blank=True)
  entry_summary = models.TextField("Summary",null=True,blank=True)
  #creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_feedsin',verbose_name ='Creator',default=defaultcreator)
  creationdate = models.DateTimeField(auto_now_add=True,db_index=True)
  entry_summary_detail_type = models.TextField("entry_Summary_detail_type",null=True,blank=True)
  entry_summary_detail_language = models.TextField("entry_Summary_detail_language",null=True,blank=True)
  entry_summary_detail_base = models.TextField("entry_title_Summary_base",null=True,blank=True)
  entry_summary_detail_value = models.TextField("entry_title_Summary_value",null=True,blank=True)
  entry_published = models.DateTimeField()
  entry_published_parsed = models.TextField("Published Parsed",null=True,blank=True)
  entry_id = models.TextField("Entry ID",null=True,blank=True)
  entry_guidislink = models.TextField("Guidislink",null=True,blank=True)
  entry_content_type = models.TextField("entry_content_type",null=True,blank=True)
  entry_content_language = models.TextField("entry_content_language",null=True,blank=True)
  entry_content_base = models.TextField("entry_content_base",null=True,blank=True)
  entry_content_value = models.TextField("entry_content_value",null=True,blank=True)
  entry_media_thumbnail_url = models.TextField("entry_media_thumbnail_url",null=True,blank=True)
  entry_media_thumbnail_width = models.TextField("entry_media_thumbnail_width",null=True,blank=True)
  entry_media_thumbnail_height = models.TextField("entry_media_thumbnail_height",null=True,blank=True)
  entry_href = models.TextField("entry_href",null=True,blank=True)
  entry_media_content_type = models.TextField("entry_media_content_type",null=True,blank=True)
  entry_media_content_url = models.TextField("entry_media_content_url",null=True,blank=True)
  entry_media_content_height = models.TextField("entry_media_content_height",null=True,blank=True)
  entry_media_content_medium = models.TextField("entry_media_content_medium",null=True,blank=True)
  entry_media_content_width = models.TextField("entry_media_content_width",null=True,blank=True)
  entry_media_credit_content = models.TextField("entry_media_credit_content",null=True,blank=True)
  entry_credit = models.TextField("entry_credit",null=True,blank=True)
  entry_authors = models.TextField("authors",null=True,blank=True)
  entry_author = models.TextField("author",null=True,blank=True)
  entry_author_detail = models.TextField("author_detail",null=True,blank=True)
  entry_tags_term = models.TextField("entry_tags_term",null=True,blank=True)
  entry_tags_scheme = models.TextField("entry_tags_scheme",null=True,blank=True)
  entry_tags_label = models.TextField("entry_tags_label",null=True,blank=True)
  feed_title = models.TextField("feed_title",null=True,blank=True)
  feed_title_detail_type = models.TextField("feed_title_detail_type",null=True,blank=True)
  feed_title_detail_language = models.TextField("feed_title_detail_language",null=True,blank=True)
  feed_title_detail_base = models.TextField("feed_title_detail_base",null=True,blank=True)
  feed_title_detail_value = models.TextField("feed_title_detail_value",null=True,blank=True)
  feed_links_rel = models.TextField("feed_links_rel",null=True,blank=True)
  feed_links_type = models.TextField("feed_links_type",null=True,blank=True)
  feed_links_href = models.TextField("feed_links_href",null=True,blank=True)
  feed_link = models.TextField("feed_link",null=True,blank=True)
  feed_image_title = models.TextField("feed_image_title",null=True,blank=True)
  feed_image_title_detail_type = models.TextField("feed_image_title_detail_type",null=True,blank=True)
  feed_image_title_detail_language = models.TextField("feed_image_title_detail_language",null=True,blank=True)
  feed_image_title_detail_base = models.TextField("feed_image_title_detail_base",null=True,blank=True)
  feed_image_title_detail_value = models.TextField("feed_image_title_detail_value",null=True,blank=True)
  feed_image_href = models.TextField("feed_image_href",null=True,blank=True)
  feed_image_link = models.TextField("feed_image_link",null=True,blank=True)
  feed_image_links = models.TextField("feed_image_links",null=True,blank=True)
  feed_subtitle = models.TextField("feed_subtitle",null=True,blank=True)
  feed_subtitle_detail = models.TextField("feed_subtitle_detail",null=True,blank=True)
  feed_language = models.ForeignKey(Speech, related_name="speech", on_delete=models.CASCADE)
  feed_rights = models.TextField("feed_rights",null=True,blank=True)
  feed_rights_detail = models.TextField("feed_rights_detail",null=True,blank=True)
  feed_updated = models.TextField("feed_updated",null=True,blank=True)
  feed_updated_parsed = models.TextField("feed_updated_parsed",null=True,blank=True)
  feed_published = models.TextField("feed_published",null=True,blank=True)
  feed_published_parsed = models.TextField("feed_published_parsed",null=True,blank=True)
  feed_tags_term = models.TextField("feed_tags_term",null=True,blank=True)
  feed_tags_scheme = models.TextField("feed_tags_scheme",null=True,blank=True)
  feed_tags_label = models.TextField("feed_tags_label",null=True,blank=True)
  feed_tags_list = models.TextField("feed_tags_list",null=True,blank=True)
  feed_ttl = models.TextField("feed_ttl",null=True,blank=True)
  feed_docs = models.TextField("feed_docs",null=True,blank=True)
  feed_generator_detail = models.TextField("generator_detail",null=True,blank=True)
  feed_generator = models.TextField("feed_generator",null=True,blank=True)
  feed_publisher = models.TextField("feed_Publisher",null=True,blank=True)
  feed_publisher_detail = models.TextField("feed_publisher_detail",null=True,blank=True)
  headers_date = models.TextField("headers date",null=True,blank=True)
  publishdate = models.DateField("Publish Date",null=True,blank=True)
  #sentiment = models.DecimalField(max_digits=4, decimal_places=2,default=0)
  sentiment = models.CharField('sentiment', max_length=8, default='neutral')
  usersentiment = models.DecimalField(max_digits=4, decimal_places=2,default=0)
  updatedsentiment = models.DecimalField(max_digits=4, decimal_places=2,default=0)
  is_sentiment = models.BooleanField(default=False)

  class Meta:
    indexes = [
      models.Index(fields=['entry_published',]),
      models.Index(fields=['entry_title',]),
      models.Index(fields=['feedlink',]),
      models.Index(fields=['entry_author',]),
      models.Index(fields=['feed_language',]),
      models.Index(fields=['sentiment',]),
      GinIndex(
        name='entry_title_gin_index',
        fields=['entry_title'],
        opclasses=['gin_trgm_ops'],
      ),
    ]
  
  def __str__(self):
    return self.entry_title

class Status(models.Model):
  progress = models.IntegerField()
