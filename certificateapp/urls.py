from django.urls import path
from . import views

app_name = "certificateapp"

urlpatterns = [
    path("generate/", views.generate_certificate, name="generate_certificate"),
    path("certificate/<str:certificate_id>/", views.view_certificate, name="view_certificate"),
]