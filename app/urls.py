from django.urls import path

from . import views

urlpatterns = [
    path('generate', views.Generate.as_view())
]
