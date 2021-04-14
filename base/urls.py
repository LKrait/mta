from django.urls import path
from . import views


urlpatterns = [
    path('src/style/css/', views.style),
]
