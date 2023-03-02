from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView



@api_view(['GET'])
def product_list_api(request):
    query = Product.objects.all()
    data = ProductSerializer(query,many=True).data
    return Response({'data': data})



class ProductListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:20]



class ProductDetailAPI(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
    lookup_field = 'slug'   