# Generated by Django 4.0.6 on 2023-03-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_components', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlcategory',
            name='category_title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
