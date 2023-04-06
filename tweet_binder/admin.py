from django.contrib import admin
from .models import *

@admin.register(HistoricalSearchProject)
class HistoricalSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyword', 'limit', 'start_date', 'end_date', 'updated_at', 'created_at')
    search_fields = ('title__startswith', 'keyword__startswith')

@admin.register(BasicSearchProject)
class BasicSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyword', 'limit', 'created_at', 'updated_at', 'created_at')
    search_fields = ('title__startswith', 'keyword__startswith')    

@admin.register(TweetBinderPost)
class TweetBinderPostAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_alias', 'post_id', 'updated_at', 'created_at')
    search_fields = ('text__startswith', 'user_name__startswith')

@admin.register(LiveSearchProject)
class LiveSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyword', 'limit', 'updated_at', 'created_at')
    search_fields = ('title__startswith', 'keyword__startswith')    

@admin.register(TweetBinderUserTracker)
class TweetBinderUserTrackerAdmin(admin.ModelAdmin):
    list_display = ('user_alias', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('user_alias',)

@admin.register(TweetBinderUserTrackerAnalysis)
class TweetBinderUserTrackerAnalysisAdmin(admin.ModelAdmin):
    list_display = ('user_alias', 'followers_start', 'followers_end', 'following_start', 'following_end', 'user_value_start', 'user_value_end')
    search_fields = ('user_alias',)
