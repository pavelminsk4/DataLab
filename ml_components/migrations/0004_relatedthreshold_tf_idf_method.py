# Generated by Django 4.0.6 on 2023-06-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_components', '0003_relatedthreshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedthreshold',
            name='tf_idf_method',
            field=models.BooleanField(default=False),
        ),
    ]
