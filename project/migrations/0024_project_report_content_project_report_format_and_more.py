# Generated by Django 4.0.6 on 2022-11-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_project_report_template_alter_project_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='report_content',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='report_format',
            field=models.CharField(default='pdf', max_length=3),
        ),
        migrations.AddField(
            model_name='project',
            name='report_language',
            field=models.CharField(default='English', max_length=10),
        ),
        migrations.AddField(
            model_name='project',
            name='report_table_content',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='report_widgets',
            field=models.BooleanField(default=True),
        ),
    ]
