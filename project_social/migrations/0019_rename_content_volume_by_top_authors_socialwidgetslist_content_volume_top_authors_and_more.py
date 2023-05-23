# Generated by Django 4.0.6 on 2023-05-10 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_social', '0018_alter_projectsocial_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialwidgetslist',
            old_name='content_volume_by_top_authors',
            new_name='content_volume_top_authors',
        ),
        migrations.RenameField(
            model_name='socialwidgetslist',
            old_name='content_volume_by_top_languages',
            new_name='content_volume_top_languages',
        ),
        migrations.RenameField(
            model_name='socialwidgetslist',
            old_name='content_volume_by_top_locations',
            new_name='content_volume_top_locations',
        ),
    ]