# Generated by Django 4.0.6 on 2023-05-04 14:15

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        wd = AccountAnalysisWidgetDescription.objects.create(title='Follower growth', default_title='Follower growth')
        wd.save()
        i.follower_growth = wd
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0009_accountanalysiswidgetslist_most_engaging_media_types_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='follower_growth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower_growth', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]
