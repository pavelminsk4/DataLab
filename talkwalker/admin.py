from django.contrib import admin
from talkwalker.models import TalkwalkerPost
from talkwalker.models import TalkwalkerFeedlink
# Register your models here.

@admin.register(TalkwalkerPost)
class TalkwalkerPostAdmin(admin.ModelAdmin):
    #list_display = ('entry_title', 'entry_summary', 'entry_links_href')
    list_display = [field.name for field in TalkwalkerPost._meta.fields if field.name != "id"]


@admin.register(TalkwalkerFeedlink)
class TalkwalkerFeedlinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TalkwalkerFeedlink._meta.fields if field.name != "id"]
