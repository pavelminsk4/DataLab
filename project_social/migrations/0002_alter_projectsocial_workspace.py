# Generated by Django 4.0.6 on 2023-03-07 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsocial',
            name='workspace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_workspace_projects', to='project_social.workspacesocial'),
        ),
    ]
