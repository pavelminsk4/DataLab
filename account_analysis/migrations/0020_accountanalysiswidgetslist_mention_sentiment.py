# Generated by Django 4.0.6 on 2023-05-25 14:27

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        wd = AccountAnalysisWidgetDescription.objects.create(title='Mention sentiment', default_title='Mention sentiment')
        wd.save()
        i.mention_sentiment = wd
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0019_accountanalysiswidgetslist_most_frequent_mention_media_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='mention_sentiment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mention_sentiment', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]
