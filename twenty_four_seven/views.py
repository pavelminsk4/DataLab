from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.http import JsonResponse
import json
from .whatsapp import *


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class TwentyFourSevenProjectViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return ProjectTwentyFourSeven.objects.filter(members=user)

        return ProjectTwentyFourSeven.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectTwentyFourSevenPostSerializer
        return ProjectTwentyFourSevenSerializer


class WorkspaceTwentyFourSevenViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return WorkspaceTwentyFourSeven.objects.filter(members=user)

        return WorkspaceTwentyFourSeven.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkspaceTwentyFourSevenPostSerializer
        return WorkspaceTwentyFourSevenSerializer


def whatsapp(request):
    body = json.loads(request.body)
    phone_number = body['phone_number']
    message_content = body['message_content']
    res = whatsappp_sender(phone_number, message_content)
    return JsonResponse(res, safe = False)
