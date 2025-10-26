from django.urls import path
from .views import (
    UserListAPI, UserDetailAPI,
    ProductListAPI, ProductDetailAPI
)

urlpatterns = [
    path('users/', UserListAPI.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),

    path('products/', ProductListAPI.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductDetailAPI.as_view(), name='product-detail'),
]
