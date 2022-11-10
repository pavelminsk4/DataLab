from django.db import models

class Templates(models.Model):
  title = models.CharField(max_length=50)
  layout_file = models.FileField(upload_to='static/report_templates')

  def __str__(self):
    return self.title
