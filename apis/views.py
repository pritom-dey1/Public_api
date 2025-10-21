from rest_framework import generics
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer

# GET list and POST (create)
class UserListCreateAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductListCreateAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
