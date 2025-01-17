# Generated by Django 4.0.6 on 2023-05-08 08:16

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        wd = AccountAnalysisWidgetDescription.objects.create(title='Optimal post length', default_title='Optimal post length')
        wd.save()
        i.optimal_post_length = wd
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0010_accountanalysiswidgetslist_follower_growth'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='optimal_post_length',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='optimal_post_length', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]
