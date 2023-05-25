# Generated by Django 4.0.6 on 2023-05-25 13:41

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        wd = AccountAnalysisWidgetDescription.objects.create(title='Most frequent mention media types', default_title='Most frequent mention media types')
        wd.save()
        i.most_frequent_mention_media_types = wd
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0018_accountanalysiswidgetslist_mention_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='most_frequent_mention_media_types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='most_frequent_mention_media_types', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]
