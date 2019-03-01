"""LvShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from goods.views import Test
from LvShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

# from goods.views import GoodsListView
from goods.view_base import RawGoodsListView

# from goods.views import GoodsListViewSet
# goods_list = GoodsListViewSet.as_view({
#     'get':'list',
# })
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^send/', Test.as_view()),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^docs/', include_docs_urls(title='我的生鲜店')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # 这个url可以在访问页面时候有login in的接口
    # url(r'goods/$',goods_list,name='goods-list'),
    url(r'^', include(router.urls)),
    url(r'rawgoods/$', RawGoodsListView.as_view(), name='rawgoods-list'),

]
