from uuid import uuid4

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mapping


class Redirect(APIView):
    def get(self, request, path):
        return redirect(get_object_or_404(Mapping, path=path).url)


class Generate(APIView):
    def post(self, request):
        data = request.data
        path = data['path'] if 'path' in data else str(uuid4())[:7]
        url = data['url']
        try:
            Mapping.objects.create(path=path, url=url)
        except Exception:
            return Response(status=409)
        return JsonResponse({'url': f'localhost:8000/redirect/{path}'}, status=201)
