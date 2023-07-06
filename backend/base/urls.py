from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes, name="getRoute"),
    path('products/', getProducts, name="getProducts"),
    path('products/<str:pk>/', getProduct, name="getProduct"),
]