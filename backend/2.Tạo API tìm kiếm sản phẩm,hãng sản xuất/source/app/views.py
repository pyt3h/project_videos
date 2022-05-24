from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, CharField, DateTimeField
from datetime import datetime
from .models import *

@api_view(['GET', 'POST'])
def hello(request):    
   return Response({"message" : "Hello world!"})

class BrandSerializer(ModelSerializer):
   class Meta:
      model = Brand
      fields = '__all__'

class ProductSerializer(ModelSerializer):
   class Meta:
      model = Product
      fields = '__all__'

   brand_name = CharField(read_only=True, source='brand.name')


@api_view(['GET'])
def get_all_brand(request):
   brand_list = Brand.objects.all()
   result = BrandSerializer(brand_list, many=True).data
   return Response(result)


@api_view(['GET'])
def search_product(request):
   params = request.GET
   keyword = params.get('keyword', '')
   brand_id = params.get('brand_id')
   min_price = params.get('min_price')
   max_price = params.get('max_price')
   start = int(params.get('start', 0))
   count = int(params.get('count', 10))
   
   product_list = Product.objects.all()

   if keyword:
      product_list = product_list.filter(name__icontains=keyword)

   if brand_id:
      product_list = product_list.filter(brand__id=brand_id)

   if min_price:
      product_list = product_list.filter(price__gte=min_price)

   if max_price:
      product_list = product_list.filter(price__lte=max_price)

   total = product_list.count()
   items = ProductSerializer(product_list[start:start+count], many=True).data
   result = {'total': total, 'items': items}
   return Response(result)

@api_view(['GET'])
def get_product_by_id(request, pk):
   product = Product.objects.filter(pk=pk).first()
   if product:
      result = ProductSerializer(product).data
      return Response(result)
   else:
      return Response({})
