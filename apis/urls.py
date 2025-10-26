from django.urls import path
from .views import (
    UserListAPI, UserDetailAPI,
    ProductListCreateAPI, ProductDetailAPI
)

urlpatterns = [
    path('users/', UserListAPI.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),

    path('products/', ProductListCreateAPI.as_view(), name='products-list-create'),
    path('products/<int:pk>/', ProductDetailAPI.as_view(), name='product-detail'),
]
