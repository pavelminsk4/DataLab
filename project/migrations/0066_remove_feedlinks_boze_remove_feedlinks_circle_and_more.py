# Generated by Django 4.0.6 on 2023-10-17 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0065_post_source_type_alter_changingonlinesentiment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedlinks',
            name='boze',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='circle',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='creationdate',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='errornotes',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='issourcefeed',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='languagecode',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='lastupdate',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='linklanguage',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='myscript',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='nooffeeds',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='page',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='source',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='status_code',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='feedlinks',
            name='updated_at',
        ),
    ]
