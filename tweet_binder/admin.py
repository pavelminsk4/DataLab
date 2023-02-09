from django.contrib import admin
from .models import TweetBinderPost, TweetBinderProject


@admin.register(TweetBinderPost)
class TweetBinderPostAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_alias', 'post_id')
    search_fields = ('text__startswith', 'user_name__startswith')

@admin.register(TweetBinderProject)
class TweetBinderProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyword', 'limit')
    search_fields = ('title', 'keyword')
