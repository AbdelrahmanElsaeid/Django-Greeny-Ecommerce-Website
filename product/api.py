from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer, BrandDetailSerializer, ProductDetailSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .mypagination import ProductPagination
from rest_framework import filters
from .myfilters import ProductFilter

@api_view(['GET'])
def product_list_api(request):
    query = Product.objects.all()
    data = ProductSerializer(query,many=True).data
    return Response({'data': data})



class ProductListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination


    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['price', 'brand']

    filterset_class =  ProductFilter
    filterset_fields = ['name']



class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all() 
    lookup_field = 'slug'   



class BrandApi(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()



class BrandDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    lookup_field = 'slug'        
