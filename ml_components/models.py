from django.db import models
from ndarraydjango.fields import NDArrayField
import numpy as np
from django.dispatch import receiver
from django.db.models.signals import post_save
from sentence_transformers import SentenceTransformer
from django.contrib.postgres.fields import ArrayField

class MlCategory(models.Model):
  category_title = models.CharField(max_length=100, unique=True)
  category_vector = ArrayField(NDArrayField(shape=(384), dtype=np.float32), blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.category_title
  

class RelatedThreshold(models.Model):
  is_active = models.BooleanField(default=False)
  description = models.CharField(max_length=100)
  threshold = models.FloatField(blank=True, null=True)
  tf_idf_method = models.BooleanField(default=False)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.description
  

@receiver(post_save, sender=MlCategory)
def calculate_category_vector(sender, instance, created, **kwargs):
  if created:
    multilingual_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    small_sum_emb = multilingual_model.encode(instance.category_title, convert_to_tensor=True)
    vector = np.array(small_sum_emb.cpu())
    instance.category_vector = [vector]
    instance.save()
