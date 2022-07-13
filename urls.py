from django.urls import path
from .views import template_familia, inicio

urlpatterns = [
    path('', inicio),
    path(
        'mi-template/<nombre>/<segundo_nombre>/<documento>/<edad>/<nacimiento>',
        template_familia
        )
]