from django.contrib import admin
from multilanguage.models import PhraseTranslations


@admin.register(PhraseTranslations)
class PhraseTranslationsAdmin(admin.ModelAdmin):
    list_display = ('en', 'ar', 'updated_at', 'created_at')
