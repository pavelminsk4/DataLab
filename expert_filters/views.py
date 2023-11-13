from expert_filters.serializers import GroupNestedSerializer
from expert_filters.serializers import GroupBasicSerializer
from expert_filters.serializers import PresetSerializer
from expert_filters.models import Group, Preset
from rest_framework import viewsets


class GroupsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Group.objects.filter(creator=user)
        return Group.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupNestedSerializer
        return GroupBasicSerializer


class PresetsViewSet(viewsets.ModelViewSet):
    serializer_class = PresetSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Preset.objects.filter(creator=user)
        return Preset.objects.none()
