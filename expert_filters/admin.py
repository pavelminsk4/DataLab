from expert_filters.models import Group, Preset
from django.contrib import admin


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creator', 'updated_at', 'created_at')


@admin.register(Preset)
class PresetAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'creator', 'updated_at', 'created_at')
