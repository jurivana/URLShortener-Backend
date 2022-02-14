from django.urls import path

from . import views

urlpatterns = [
    path('redirect/<str:path>', views.Redirect.as_view()),
    path('generate', views.Generate.as_view())
]
