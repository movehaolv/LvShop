from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.core.mail import send_mail
from django.shortcuts import HttpResponse

class Test(View):
    def get(self,request):
        send_mail('Subject here', 'Here is the message.', '839985880@qq.com',
                  ['839985880@qq.com'], fail_silently=False)
        return HttpResponse('ok')



from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods
from rest_framework import status

from rest_framework.pagination import PageNumberPagination
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


from rest_framework import generics
class GoodsListView(generics.ListAPIView):
    # 更加精简的展示商品列表
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination




# class GoodsListView(APIView):
#     """
#     List all goods.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:5]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
