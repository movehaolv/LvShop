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



from .serializers import GoodsSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods,GoodsCategory
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


from rest_framework import mixins,viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters
class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # 配置filter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')   # 这样前段filter的时候只能完全匹配过滤，无法模糊或设定区间匹配
    # 建立filter.py文件，对需要字段进行模糊匹配,这种过滤方式需要查看github上django-filter的操作
    filter_class = GoodsFilter
    # 给过滤器添加搜索框进行模糊搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 给字段进行排序
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    RetrieveModelMixin 参数可以使得前端输入http://127.0.0.1:8000/categorys/1/而显示id为1的商品，相当于restful接口的GET操作 GET /zoos/ID：获取某个指定动物园的信息
    list:
        商品分类列表
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer




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
