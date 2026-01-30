from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("chembl/", views.chembl_view, name="chembl"),
    path("povray/", views.povray_view, name="povray"),
]




