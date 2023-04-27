from django.contrib import admin
from .models import Templates, RegularReport, ReportItem

admin.site.register(Templates)
admin.site.register(ReportItem)

@admin.register(RegularReport)
class RegularReportAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'hourly_enabled',
        'h_template',
        'daily_enabled',
        'd_template',
        'weekly_enabled',
        'w_template',
        'monthly_enabled',
        'm_template',
        'created_at',
        'updated_at',
        )

