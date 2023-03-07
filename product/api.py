from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer, BrandDetailSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView, RetrieveUpdateDestroyAPIView



@api_view(['GET'])
def product_list_api(request):
    query = Product.objects.all()
    data = ProductSerializer(query,many=True).data
    return Response({'data': data})



class ProductListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:20]



class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
    lookup_field = 'slug'   



class BrandApi(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()



class BrandDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    lookup_field = 'slug'        
