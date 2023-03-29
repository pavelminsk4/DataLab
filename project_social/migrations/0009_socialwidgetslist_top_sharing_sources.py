# Generated by Django 4.0.6 on 2023-03-29 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_social', '0008_socialwidgetslist_sentiment_diagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialwidgetslist',
            name='top_sharing_sources',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_top_sharing_sources', to='project_social.socialwidgetdescription'),
        ),
    ]
