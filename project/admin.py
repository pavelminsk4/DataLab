from django.contrib import admin
from .models import Project, Workspace, Feedlinks, Post, Speech, Status, TempFeedLinks, NewFeedlinks, CrawlerKeyword
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.register(Project)
admin.site.register(Workspace)
admin.site.register(Speech)
admin.site.register(Status)
admin.site.register(CrawlerKeyword)

def make_approved(modeladmin, request, queryset):
    queryset.update(is_approved=True)
make_approved.short_description = "Mark selected feeds as approved."

def move_approved(modeladmin, request, queryset):
  for link in queryset:
    if link.is_approved:
      feed, created = Feedlinks.objects.get_or_create(
        url = link.url
      )
      feed.source1 = link.source1
      feed.sourceurl = link.sourceurl
      feed.county = link.country
      feed.save()
      link.delete()
move_approved.short_description = "Move the selected feeds to the common scope of Feedlinks."

@admin.register(NewFeedlinks)
class NewFeedlinksAdmin(admin.ModelAdmin):
    list_display = ('source1', 'url', 'sourceurl', 'country', 'is_approved', 'created_at', 'updated_at')
    search_fields = ('source1__startswith', 'url__startswith', 'sourceurl__startswith')
    actions = [make_approved, move_approved]
    
# === Feedlinks Import-Export
class FeedlinksResource(resources.ModelResource):
  class Meta:
    model = Feedlinks

  def skip_row(self, instance, original):
    return Feedlinks.objects.filter(url=instance.url).exists()

class FeedlinksAdmin(ImportExportModelAdmin):
  resource_class = FeedlinksResource
  list_display = ('source1', 'url', 'sourceurl', 'country', 'tier', 'errornotes', 'nooffeeds', 'created_at', 'updated_at')
  search_fields = ('source1__startswith', 'url__startswith', 'sourceurl__startswith')

admin.site.register(Feedlinks, FeedlinksAdmin )

# ==== Post Import-Export
class PostResource(resources.ModelResource):
  class Meta:
    model = Post

class PostAdmin(ImportExportModelAdmin):
  resource_class = PostResource

admin.site.register(Post, PostAdmin)

# ==== TempFeedLinks ===

class TempFeedLinksResource(resources.ModelResource):
  class Meta:
    model = TempFeedLinks

class TempFeedLinksAdmin(ImportExportModelAdmin):
  resource_class = TempFeedLinksResource

admin.site.register(TempFeedLinks, TempFeedLinksAdmin)
