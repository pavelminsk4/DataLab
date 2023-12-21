from twenty_four_seven.models import Item, ProjectTwentyFourSeven
from twenty_four_seven.serializers import ItemSerializer, ItemPatchSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size             = 100
    max_page_size         = 1000


class ItemViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if not self.request.GET:
            return Item.objects.all()

        status = self.request.GET.get('status')
        order  = self.request.GET.get('order')

        options = {
            'asc_date': 'post__entry_published',
            'desc_date': '-post__entry_published',
            'asc_reach': 'post__feedlink__alexaglobalrank',
            'desc_reach': '-post__feedlink__alexaglobalrank',
        }

        return Item.objects.filter(project__pk=self.kwargs['project_pk'], status=status).order_by(options[order])

    def get_serializer_class(self):
        return ItemPatchSerializer if self.request.method == 'PATCH' else ItemSerializer

    def retrieve(self, request, project_pk, pk):
        project = get_object_or_404(ProjectTwentyFourSeven, pk=project_pk)
        item    = get_object_or_404(project.tfs_project_items, pk=pk)

        return Response(ItemSerializer(item).data)

    pagination_class = StandardResultsSetPagination
