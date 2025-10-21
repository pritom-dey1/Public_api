from django.urls import path
from .views import UserListCreateAPI, ProductListCreateAPI

urlpatterns = [
    path('users/', UserListCreateAPI.as_view(), name='users-list-create'),
    path('products/', ProductListCreateAPI.as_view(), name='products-list-create'),
]
