from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class NewFeedlinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'triggered_on_every_n_new_posts', 'how_many_posts_to_send', 'privious_posts_count', 'created_at', 'updated_at')
