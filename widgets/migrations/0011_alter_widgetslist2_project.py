# Generated by Django 4.0.6 on 2022-11-25 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0027_alter_project_author_filter_and_more'),
        ('widgets', '0010_widgetslist2_clipping_widget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetslist2',
            name='project',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='widgets_list_2', to='project.project'),
        ),
    ]
