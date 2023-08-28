from expert_filters.serializers import GroupSerializer, GroupPostSerializer, PresetSerializer, PresetPostSerializer
from expert_filters.models import Group, Preset
from rest_framework import viewsets


class GroupsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Group.objects.filter(creator=user)
        return Group.objects.none()

    def get_serializer_class(self):
        return GroupSerializer


class PresetsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        group = self.kwargs['group_pk']
        user = self.request.user
        if not user.is_anonymous:
            return Preset.objects.filter(creator=user).filter(group=group)
        return Preset.objects.none()

    def get_serializer_class(self):
        return PresetSerializer
