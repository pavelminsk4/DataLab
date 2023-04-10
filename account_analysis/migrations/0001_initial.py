# Generated by Django 4.0.6 on 2023-04-10 12:22

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0010_department_current_number_of_account_analysis_projects_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAnalysisWidgetDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('title', models.CharField(default='Title', max_length=50)),
                ('default_title', models.CharField(default='Default Title', max_length=50)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('aggregation_period', models.CharField(default='day', max_length=10)),
                ('country_dimensions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None)),
                ('language_dimensions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None)),
                ('sentiment_dimensions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None)),
                ('chart_type', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('top_counts', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='WorkspaceAccountAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='account_analysis_workspaces', to='accounts.department')),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAccountAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_handle', models.CharField(max_length=100)),
                ('start_search_date', models.DateTimeField()),
                ('end_search_date', models.DateTimeField()),
                ('min_followers', models.IntegerField(default=0)),
                ('max_followers', models.IntegerField(default=1000000000)),
                ('language_filter', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None)),
                ('country_filter', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None)),
                ('sentiment_filter', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_account_analysis', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, null=True, related_name='projects_account_analysis', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_analysis_workspace_projects', to='account_analysis.workspaceaccountanalysis')),
            ],
        ),
        migrations.CreateModel(
            name='AccountAnalysisWidgetsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='account_analysis_widgets_list', to='account_analysis.projectaccountanalysis')),
                ('summary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_analysis_summary', to='account_analysis.accountanalysiswidgetdescription')),
            ],
        ),
    ]
