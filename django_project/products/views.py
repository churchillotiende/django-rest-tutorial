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

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self,serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content = content)
