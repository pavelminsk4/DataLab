# Generated by Django 4.0.6 on 2023-04-27 09:18

from django.db import migrations, models
import django.db.models.deletion

def populate_new_columns(apps, schema_editor):
    AccountAnalysisWidgetsList = apps.get_model('account_analysis', 'AccountAnalysisWidgetsList')
    AccountAnalysisWidgetDescription = apps.get_model('account_analysis', 'AccountAnalysisWidgetDescription')
    wl = AccountAnalysisWidgetsList.objects.all()
    for i in wl:
        w = AccountAnalysisWidgetDescription.objects.create(title='Most frequent post types', default_title='Most frequent post types')
        w.save()
        i.most_frequent_post_types = w
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0004_accountanalysiswidgetslist_profile_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountanalysiswidgetslist',
            name='most_frequent_post_types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_analysis_most_frequent_post_types', to='account_analysis.accountanalysiswidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]