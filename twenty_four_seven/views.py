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


class WorkspaceTwentyFourSevenlList(ListAPIView):
    serializer_class = WorkspaceTwentyFourSevenSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return WorkspaceTwentyFourSeven.objects.filter(members=user)

        return WorkspaceTwentyFourSeven.objects.none()


class WorkspaceTwentyFourSevenCreate(CreateAPIView):
    queryset = WorkspaceTwentyFourSeven.objects.all()
    serializer_class = WorkspaceTwentyFourSevenCreateSerializer


class WorkspaceTwentyFourSevenUpdate(UpdateAPIView):
    queryset = WorkspaceTwentyFourSeven.objects.all()
    serializer_class = WorkspaceTwentyFourSevenSerializer


class WorkspaceTwentyFourSevenDelete(DestroyAPIView):
    queryset = WorkspaceTwentyFourSeven.objects.all()
    serializer_class = WorkspaceTwentyFourSevenSerializer


class TwentyFourSevenProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectTwentyFourSeven.objects.all()
    serializer_class = ProjectTwentyFourSevenSerializer


def whatsapp(request):
    body = json.loads(request.body)
    phone_number = body['phone_number']
    message_content = body['message_content']
    res = whatsappp_sender(phone_number, message_content)
    return JsonResponse(res, safe = False)
