from django.contrib import admin
from .models import Project, Workspace, Company, Feedlinks
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.register(Project)
admin.site.register(Workspace)
admin.site.register(Company)


class FeedlinksResource(resources.ModelResource):
  class Meta:
    model = Feedlinks

class FeedlinksAdmin(ImportExportModelAdmin):
   resource_class = FeedlinksResource

admin.site.register(Feedlinks, FeedlinksAdmin )
