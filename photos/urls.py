from django.urls import path
from . import views

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("add/", views.addPhoto, name="addPhoto"),
    path("viewphoto/<str:pk>/", views.viewPhoto, name="viewPhoto"),
]
