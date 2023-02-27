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
