# Generated by Django 4.0.6 on 2023-05-29 08:44

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        wd = AccountAnalysisWidgetDescription.objects.create(title='Mention summary', default_title='Mention summary')
        wd.save()
        i.mention_summary = wd
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0021_accountanalysiswidgetslist_top_mentions_by_engagements'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='mention_summary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mention_summary', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]
