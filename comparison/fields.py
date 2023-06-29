from project_social.models import ProjectSocial
from rest_framework import serializers
from project.models import Project

class ProjectNameField(serializers.Field):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, value):
        models = {
            'Project': Project,
            'ProjectSocial': ProjectSocial,
        }
        return models[value.module_type].objects.get(id=value.module_project_id).title
