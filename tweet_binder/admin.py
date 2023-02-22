from django.contrib import admin
from .models import TweetBinderPost, HistoricalSearchProject, BasicSearchProject

@admin.register(HistoricalSearchProject)
class HistoricalSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyword', 'created_at', 'limit', 'start_date', 'end_date')
    search_fields = ('title__startswith', 'keyword__startswith')

@admin.register(BasicSearchProject)
class BasicSearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyword', 'created_at', 'limit')
    search_fields = ('title__startswith', 'keyword__startswith')    

@admin.register(TweetBinderPost)
class TweetBinderPostAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_alias', 'post_id')
    search_fields = ('text__startswith', 'user_name__startswith')
