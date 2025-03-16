from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListCreateAPIView):
  """
   List all products, or create a new one.
  """
  model = Product
  serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = Product.objects.all()
    serializer_class  =ProductSerializer