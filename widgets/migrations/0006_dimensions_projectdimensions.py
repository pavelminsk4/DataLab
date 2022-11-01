# Generated by Django 4.0.6 on 2022-11-02 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_post_entry_title_gin_index'),
        ('widgets', '0005_widgetdescription_widgetslist2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimensions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDimensions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widgets.dimensions', verbose_name='Dimension')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='Project')),
            ],
        ),
    ]
