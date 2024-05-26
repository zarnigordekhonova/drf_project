from django.urls import path
from .views import ListCategoryAPIView, ListProductsAPIView

urlpatterns = [
    path('category_list/', ListCategoryAPIView.as_view(), name='category_list'),
    path('products_list/', ListProductsAPIView.as_view(), name='products_list'),

]