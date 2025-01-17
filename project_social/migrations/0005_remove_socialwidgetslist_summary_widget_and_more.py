# Generated by Django 4.0.6 on 2023-03-14 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_social', '0004_remove_socialwidgetslist_content_volume_by_top_countries_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialwidgetslist',
            name='summary_widget',
        ),
        migrations.AddField(
            model_name='socialwidgetdescription',
            name='top_counts',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='socialwidgetslist',
            name='summary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_summary', to='project_social.socialwidgetdescription'),
        ),
    ]
