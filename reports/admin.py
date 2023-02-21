from django.contrib import admin
from .models import Templates, RegularReport

admin.site.register(Templates)

@admin.register(RegularReport)
class RegularReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'hourly_enabled', 'daily_enabled', 'weekly_enabled', 'monthly_enabled', 'created_at', 'updated_at')
