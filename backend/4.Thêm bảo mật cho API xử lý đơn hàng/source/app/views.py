from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, CharField, DateTimeField
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
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


@api_view(['POST'])
def save_order(request):
   data = request.data
   customer_name = data.get('customer_name')
   customer_phone = data.get('customer_phone')
   customer_address = data.get('customer_address')
   qty = data.get('qty')
   product_id = data.get('product_id')
   product = Product.objects.filter(pk=product_id).first()

   if not customer_name:
      return Response({'error': 'Họ tên là bắt buộc'}, status=500)

   if not customer_phone:
      return Response({'error': 'SĐT là bắt buộc'}, status=500)

   if not customer_address:
      return Response({'error': 'Địa chỉ là bắt buộc'}, status=500)

   if not qty:
      return Response({'error': 'Số lượng không hợp lệ'}, status=500)

   if not product:
      return Response({'error': 'Sản phẩm không tồn tại'}, status=404)

   Order.objects.create(
      customer_name=customer_name,
      customer_phone=customer_phone,
      customer_address=customer_address,
      qty=qty,
      product=product,
      price_unit=product.price,
      total=qty*product.price,
      order_date=datetime.now(),
      status=Order.OrderStatus.PENDING
   )

   return Response({'success': True})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def confirm_order(request, pk):
   order = Order.objects.get(pk=pk)
   order.status = Order.OrderStatus.DELIVERED
   order.deliver_date = datetime.now()
   order.save()
   return Response({'success': True})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_order(request, pk):
   order = Order.objects.get(pk=pk)
   order.status = Order.OrderStatus.CANCELED
   order.save()
   return Response({'success': True})

class OrderSerializer(ModelSerializer):
   class Meta:
      model = Order
      fields = '__all__'
   
   order_date = DateTimeField(read_only=True, format='%H:%M:%S %d/%m/%Y')
   deliver_date = DateTimeField(read_only=True, format='%H:%M:%S %d/%m/%Y')
   product_name = CharField(read_only=True, source='product.name')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_order(request):
   keyword = request.GET.get('keyword', '')
   order_list = Order.objects.filter(
      Q(customer_name__icontains=keyword) |
      Q(customer_phone__icontains=keyword) |
      Q(product__name__icontains=keyword)
   )
   result = OrderSerializer(order_list, many=True).data
   return Response(result)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_by_id(request, pk):
   order = Order.objects.filter(pk=pk).first()
   if order:
      result = OrderSerializer(order).data
      return Response(result)
   else:
      return Response({})