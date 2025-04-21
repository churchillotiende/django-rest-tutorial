from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListCreateAPIView):
  """
   List all products, or create a new one.
  """
  model = Product
  queryset = Product.objects.all()

  serializer_class = ProductSerializer

product_list_view = ProductListView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = Product.objects.all()
    serializer_class  =ProductSerializer

#Update view
class ProductUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "pk"
    queryset = Product.objects.all()
    serializer_class  =ProductSerializer

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            istance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

#destroy view
class ProductDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "pk"
    queryset = Product.objects.all()
    serializer_class  =ProductSerializer

    def perform_destroy(self,instance):
       #instance
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self,serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content = content)
