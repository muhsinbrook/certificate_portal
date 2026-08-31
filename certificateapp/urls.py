from django.urls import path
from . import views

app_name = "certificateapp"

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "generate/",
        views.generate_certificate,
        name="generate_certificate",
    ),

    path(
        "certificate/<str:certificate_id>/",
        views.view_certificate,
        name="view_certificate",
    ),

    path(
        "verify/",
        views.verify_certificate,
        name="verify_certificate",
    ),
]