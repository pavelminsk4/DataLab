from django.contrib import admin
from .models import *

@admin.register(ProjectAccountAnalysis)
class ProjectAccountAnalysisAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'profile_handle', 'workspace', 'start_search_date', 'end_search_date', 'created_at')
    search_fields = ('title', 'creator', 'profile_handle', 'workspace', 'start_search_date', 'end_search_date', 'created_at')

@admin.register(WorkspaceAccountAnalysis)
class WorkspaceAccountAnalysisAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'created_at')
    search_fields = ('title', 'department')

admin.site.register(AccountAnalysisWidgetDescription)
admin.site.register(AccountAnalysisWidgetsList)
