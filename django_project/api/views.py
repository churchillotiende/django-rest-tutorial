from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def api_home(request,*args,**kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"Not good data"})