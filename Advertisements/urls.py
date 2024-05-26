from django.urls import path
from .views import ListCategoryAPIView, ListProductsAPIView, DetailProductsAPIView, ProductsListAPIView

urlpatterns = [
    path('category_list/', ListCategoryAPIView.as_view(), name='category_list'),
    path('products-list/', ProductsListAPIView.as_view(), name='products-list'),
    path('products_list/', ListProductsAPIView.as_view(), name='products_list'),
    path('products_detail_list/<int:pk>/', DetailProductsAPIView.as_view(), name='products_detail_list')

]