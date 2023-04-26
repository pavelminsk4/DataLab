# Generated by Django 4.0.6 on 2023-04-26 11:40

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        w = AccountAnalysisWidgetDescription.objects.create(title='Profile timeline', default_title='Profile timeline')
        w.save()
        i.profile_timeline = w
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0003_accountanalysiswidgetdescription_author_dimensions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='profile_timeline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_analysis_profile_timeline', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]
