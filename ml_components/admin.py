from django.contrib import admin
from .models import *

@admin.register(MlCategory)
class MlCategoryAdmin(admin.ModelAdmin):
  list_display = ('category_title', 'updated_at', 'created_at')
  search_fields = ['category_title']
  
admin.site.register(RelatedThreshold)
