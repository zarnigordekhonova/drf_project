from django.shortcuts import render
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductsSerializer, ProductsDetailSerializer
from .models import Category, Products

from rest_framework.views import APIView
# Create your views here.


class ListCategoryAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class ListProductsAPIView(APIView):
    def get(self, request):
        category = Products.objects.all()
        serializer = ProductsSerializer(category, many=True)
        return Response(serializer.data)


# class DetailProductsAPIView(APIView):
#     def get(self, request, pk):
#         category = Products.objects.get(pk=pk)
#         serializer = ProductsDetailSerializer(category)
#         return Response(serializer.data)
