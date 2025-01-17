# Generated by Django 4.0.6 on 2023-05-04 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_department_current_number_of_account_analysis_projects_and_more'),
        ('project', '0050_alter_project_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangingSentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.CharField(max_length=10, verbose_name='sentiment')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.post')),
            ],
        ),
    ]
