from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'module_type',
        'module_project_id',
        'creator',
        'department',
        'triggered_on_every_n_new_posts',
        'how_many_posts_to_send',
        'privious_posts_count',
        'created_at',
        'updated_at',
        )
