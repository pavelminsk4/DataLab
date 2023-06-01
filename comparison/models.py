from django.db import models
from django.contrib.auth.models import User


class WorkspaceComparison(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    members = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True, related_name='comparison_workspaces')

    def __str__(self):
        return self.title


class ProjectComparison(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name='creator_cmpr', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    workspace = models.ForeignKey(WorkspaceComparison, related_name='cmpr_workspace_projects', blank=True, null=True, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects_cmpr', blank=True)

    def __str__(self):
        return self.title


class ComparisonItem(models.Model):
    MODULE_TYPE_CHOICES = [
        ('Project', 'Online'),
        ('ProjectSocial', 'Social'),
    ]
    module_type = models.CharField(max_length=70)
    module_project_id = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey(ProjectComparison, related_name='cmpr_items', on_delete=models.SET_NULL, null=True)
