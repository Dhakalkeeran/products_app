from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name="search-products")     # leads to views.search method
]