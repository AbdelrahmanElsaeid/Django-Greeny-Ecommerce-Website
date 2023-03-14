from django.urls import path
from .views import ProductList, ProductDetail, add_review, BrandList, BrandDetail, Product_list_debug 
from .api import product_list_api, ProductListApi, ProductDetailAPI, BrandApi, BrandDetailApi
app_name = 'product'

urlpatterns = [
    #api
    path('api/list',product_list_api),
    path('api/list/cbv', ProductListApi.as_view()),
    path('api/list/cbv/brands', BrandApi.as_view()),
    path('api/list/cbv/brands/<slug:slug>', BrandDetailApi.as_view()),

    path('api/list/cbv/<slug:slug>', ProductDetailAPI.as_view()),



    path('', ProductList.as_view(),name='product_list'),
    path('debug', Product_list_debug, name='product_list_debug'),

    path('<slug:slug>', ProductDetail.as_view(),name='product_detail'),
    path('<slug:slug>/add-review',add_review ,name='add_review'),
    path('brands/', BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>',BrandDetail.as_view(), name='brand_detail' ),



]