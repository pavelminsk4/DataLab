# Generated by Django 4.0.6 on 2022-12-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0028_alter_project_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempFeedLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True, unique=True)),
                ('alexaglobalrank', models.BigIntegerField()),
            ],
        ),
    ]
