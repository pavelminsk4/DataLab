# Generated by Django 4.0.6 on 2023-05-22 13:36

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        wd = AccountAnalysisWidgetDescription.objects.create(title='Best times to post', default_title='Best times to post')
        wd.save()
        i.best_times_to_post = wd
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0016_accountanalysiswidgetslist_top_posts_by_engagements'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='best_times_to_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_times_to_post', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]
