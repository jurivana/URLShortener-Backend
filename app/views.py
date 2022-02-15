from uuid import uuid4

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mapping


class Generate(APIView):
    def post(self, request):
        data = request.data
        path = data['path'] if 'path' in data else str(uuid4())[:7]
        url = data['url']
        try:
            Mapping.objects.create(path=path, url=url)
        except Exception:
            return Response(status=409)
        return JsonResponse({'url': f'jrvn.de/{path}'}, status=201)
