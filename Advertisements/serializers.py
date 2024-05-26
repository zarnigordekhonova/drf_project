from rest_framework import serializers
from .models import Category, Products


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'



class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name']


class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'description', 'image', 'video', 'audio', 'dock']
