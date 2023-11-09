from django.contrib import admin
from .models import *

@admin.register(EnterpriseSearchProject)
class EnterpriseSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'limit', 'start_date', 'end_date', 'updated_at', 'created_at')
    search_fields = ('title__startswith',)

@admin.register(BasicSearchProject)
class BasicSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'limit', 'created_at', 'updated_at', 'created_at')
    search_fields = ('title__startswith',)    

@admin.register(TweetBinderPost)
class TweetBinderPostAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_alias', 'post_id', 'updated_at', 'created_at')
    search_fields = ('text__startswith', 'user_name__startswith')

@admin.register(LiveSearchProject)
class LiveSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'limit', 'updated_at', 'created_at')
    search_fields = ('title__startswith',)    

@admin.register(TweetBinderUserTracker)
class TweetBinderUserTrackerAdmin(admin.ModelAdmin):
    list_display = ('user_alias', 'start_date', 'end_date', 'created_at', 'updated_at', 'account_analysis_project_id')
    search_fields = ('user_alias', 'account_analysis_project_id')

@admin.register(TweetBinderUserTrackerAnalysis)
class TweetBinderUserTrackerAnalysisAdmin(admin.ModelAdmin):
    list_display = ('user_alias', 'followers_start', 'followers_end', 'following_start', 'following_end', 'user_value_start', 'user_value_end')
    search_fields = ('user_alias',)

@admin.register(LiveReport)
class LiveReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'start_date', 'end_date', 'created_at')
    search_fields = ('report_id', 'start_date', 'end_date')
