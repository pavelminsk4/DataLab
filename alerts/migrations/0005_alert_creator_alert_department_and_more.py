# Generated by Django 4.0.6 on 2023-04-11 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def populate_new_columns(apps, schema_editor):
    Alert = apps.get_model('alerts', 'Alert')
    alerts = Alert.objects.all()
    for a in alerts:
        a.creator = a.project.creator
        a.module_project_id = a.project.id
        a.department = a.creator.user_profile.department
        a.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_department_current_number_of_account_analysis_projects_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alerts', '0004_alert_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alert_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alert',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.department'),
        ),
        migrations.AddField(
            model_name='alert',
            name='module_project_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert',
            name='module_type',
            field=models.CharField(choices=[('Project', 'Online'), ('ProjectSocial', 'Social')], default='Project', max_length=70),
            preserve_default=False,
        ),
         migrations.RunPython(
            code=populate_new_columns,
            reverse_code=migrations.RunPython.noop
        ),
    ]