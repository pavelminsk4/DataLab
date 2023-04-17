# Generated by Django 4.0.6 on 2023-03-31 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    def populate_new_columns(apps, schema_editor):
        SocialWidgetsList = apps.get_model('project_social', 'SocialWidgetsList')
        SocialWidgetDescriptions = apps.get_model('project_social', 'SocialWidgetDescription')
        wl = SocialWidgetsList.objects.all()
        for i in wl:
            w = SocialWidgetDescriptions.objects.create(title='Top authors by gender', default_title='Top authors by gender')
            w.save()
            i.top_authors_by_gender = w
            i.save()

    dependencies = [
        ('project_social', '0010_socialwidgetslist_overall_top_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialwidgetslist',
            name='top_authors_by_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_top_authors_by_gender', to='project_social.socialwidgetdescription'),
        ),
        migrations.RunPython(code=populate_new_columns, reverse_code=migrations.RunPython.noop),
    ]