from uuid import uuid4

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mapping


class Generate(APIView):
    def post(self, request):
        data = request.data
        if 'url' not in data:
            return Response(status=400)
        path = data['path'] if 'path' in data else str(uuid4())[:7]
        url = data['url']
        try:
            Mapping.objects.create(url=url, path=path)
        except Exception:
            return Response(status=409)
        return JsonResponse({'url': f'jrvn.de/{path}'}, status=201)
