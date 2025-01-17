from django.contrib import admin
from .models import Project, Workspace, Feedlinks, Post, Speech, Status, TempFeedLinks, NewFeedlinks, CrawlerKeyword, CrawlerOption
from import_export.admin import ImportExportModelAdmin
from import_export import resources


admin.site.register(Workspace)
admin.site.register(Status)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'creator', 'created_at')
    exclude = ('posts',)


def make_approved(modeladmin, request, queryset):
    queryset.update(is_approved=True)

make_approved.short_description = 'Mark selected feeds as approved.'


def move_approved(modeladmin, request, queryset):
    for link in queryset:
        if link.is_approved:
            feed, created = Feedlinks.objects.get_or_create(url=link.url)
            feed.source1 = link.source1
            feed.sourceurl = link.sourceurl
            feed.county = link.country
            feed.save()
            link.delete()

move_approved.short_description = 'Move the selected feeds to the common scope of Feedlinks.'


@admin.register(Speech)
class SpeechesAdmin(admin.ModelAdmin):
    list_display = ('language', 'country')


@admin.register(NewFeedlinks)
class NewFeedlinksAdmin(admin.ModelAdmin):
    list_display = ('source1', 'url', 'sourceurl', 'country', 'is_approved', 'created_at', 'updated_at')
    search_fields = ('source1__startswith', 'url__startswith', 'sourceurl__startswith')
    actions = [make_approved, move_approved]


@admin.register(CrawlerKeyword)
class CrawlerKeywordAdmin(admin.ModelAdmin):
    list_display = ('word', 'created_at', 'updated_at')


@admin.register(CrawlerOption)
class CrawlerOptionAdmin(admin.ModelAdmin):
    list_display = ('location', 'tbm', 'gl', 'safe', 'is_active', 'created_at', 'updated_at')


class FeedlinksResource(resources.ModelResource):
    class Meta:
        model = Feedlinks

    def skip_row(self, instance, original):
        return Feedlinks.objects.filter(url=instance.url).exists()


class FeedlinksAdmin(ImportExportModelAdmin):
    resource_class = FeedlinksResource
    list_display = ('source1', 'url', 'country')
    search_fields = ('source1__startswith', 'url__startswith')

admin.site.register(Feedlinks, FeedlinksAdmin)


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource
    list_display = ('entry_title', 'creationdate')

admin.site.register(Post, PostAdmin)


class TempFeedLinksResource(resources.ModelResource):
    class Meta:
        model = TempFeedLinks


class TempFeedLinksAdmin(ImportExportModelAdmin):
    resource_class = TempFeedLinksResource

admin.site.register(TempFeedLinks, TempFeedLinksAdmin)
