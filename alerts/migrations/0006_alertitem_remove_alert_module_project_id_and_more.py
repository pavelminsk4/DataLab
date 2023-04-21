# Generated by Django 4.0.6 on 2023-04-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_alert_creator_alert_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_type', models.CharField(choices=[('Project', 'Online'), ('ProjectSocial', 'Social')], max_length=70)),
                ('module_project_id', models.IntegerField()),
                ('previous_posts_count', models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='alert',
            name='module_project_id',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='module_type',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='privious_posts_count',
        ),
        migrations.AddField(
            model_name='alert',
            name='items',
            field=models.ManyToManyField(null=True, related_name='alert', to='alerts.alertitem'),
        ),
    ]
