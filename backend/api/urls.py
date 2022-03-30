from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home)
]
# maps endpoints for localhost:8000/api/
