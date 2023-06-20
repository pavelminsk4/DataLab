from twenty_four_seven.models import WorkspaceTwentyFourSeven
from twenty_four_seven.models import ProjectTwentyFourSeven
from twenty_four_seven.models import WARecipient
from twenty_four_seven.models import Item
from django.contrib import admin


admin.site.register(ProjectTwentyFourSeven)
admin.site.register(WorkspaceTwentyFourSeven)
admin.site.register(Item)

@admin.register(WARecipient)
class WARecipientdAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'created_at', 'updated_at')
