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

class GoodsListView(APIView):
    """
    List all goods.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

