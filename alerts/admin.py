from django.contrib import admin
from .models import Alert, AlertItem

@admin.register(Alert)
class AlertsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'creator',
        'department',
        'triggered_on_every_n_new_posts',
        'how_many_posts_to_send',
        'created_at',
        'updated_at',
    )

@admin.register(AlertItem)
class AlertItemAdmin(admin.ModelAdmin):
    list_display = (
        'module_type',
        'module_project_id',
        'previous_posts_count',
        'alert',
    )
