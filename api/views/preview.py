from api.services.preview_service import PreviewPosts
from django.http import JsonResponse


def get_posts(request):
    return JsonResponse(PreviewPosts().get(request), safe=False)
