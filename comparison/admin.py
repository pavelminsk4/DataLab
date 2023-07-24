from django.contrib import admin
from .models import *

@admin.register(ProjectComparison)
class ProjectAccountAnalysisAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'workspace')
    search_fields = ('title', 'creator', 'workspace')

@admin.register(WorkspaceComparison)
class WorkspaceAccountAnalysisAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'created_at')
    search_fields = ('title', 'department')

admin.site.register(ComparisonWidgetDescription)
admin.site.register(ComparisonItem)
