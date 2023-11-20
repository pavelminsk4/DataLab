from twenty_four_seven.models import WorkspaceTwentyFourSeven
from twenty_four_seven.models import ProjectTwentyFourSeven
from twenty_four_seven.models import WARecipient
from twenty_four_seven.models import Item
from django.contrib import admin


@admin.register(WorkspaceTwentyFourSeven)
class WorkspaceTwentyFourSeven(admin.ModelAdmin):
    list_display = ('title', 'department', 'updated_at', 'created_at')


@admin.register(ProjectTwentyFourSeven)
class ProjectTwentyFourSevenAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'creator', 'updated_at', 'created_at')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('post', 'social_post', 'status', 'project')


@admin.register(WARecipient)
class WARecipientdAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'updated_at', 'created_at')
