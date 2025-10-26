from rest_framework import generics
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer

# ===============================
# USER API (Read Only)
# ===============================
class UserListAPI(generics.ListAPIView):
    """Only GET all users with ?limit support"""
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        limit = self.request.query_params.get('limit')
        if limit and limit.isdigit():
            queryset = queryset[:int(limit)]
        return queryset


class UserDetailAPI(generics.RetrieveAPIView):
    """Only GET single user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ===============================
# PRODUCT API (Full CRUD)
# ===============================
class ProductListCreateAPI(generics.ListCreateAPIView):
    """GET list and POST create with ?limit support"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        limit = self.request.query_params.get('limit')
        if limit and limit.isdigit():
            queryset = queryset[:int(limit)]
        return queryset


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """GET single, PUT/PATCH update, DELETE"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
