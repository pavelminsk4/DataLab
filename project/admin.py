from django.contrib import admin
from .models import Project, Workspace, Company, Feedlinks, Post, Speech, Status, TempFeedLinks
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.register(Project)
admin.site.register(Workspace)
admin.site.register(Company)
admin.site.register(Speech)
admin.site.register(Status)

# === Feedlinks Import-Export
class FeedlinksResource(resources.ModelResource):
  class Meta:
    model = Feedlinks

  def skip_row(self, instance, original):
    return True if Feedlinks.objects.filter(url=instance.url).exists() else False

class FeedlinksAdmin(ImportExportModelAdmin):
  resource_class = FeedlinksResource

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
