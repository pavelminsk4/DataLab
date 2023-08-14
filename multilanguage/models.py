from django.db import models


class PhraseTranslations(models.Model):
    en = models.TextField(unique=True)
    ar = models.TextField(default=None, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
