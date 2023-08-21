from import_export.admin import ImportExportModelAdmin
from multilanguage.models import PhraseTranslations
from import_export import resources
from django.contrib import admin


class PhraseTranslationsResource(resources.ModelResource):
    class Meta:
        model = PhraseTranslations


class PhraseTranslationsAdmin(ImportExportModelAdmin):
    resource_class = PhraseTranslationsResource
    list_display = ('en', 'ar', 'updated_at', 'created_at')
    search_fields = ('en', 'ar')


admin.site.register(PhraseTranslations, PhraseTranslationsAdmin)
