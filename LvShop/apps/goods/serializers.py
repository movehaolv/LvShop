#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/10 17:17 
# @Author : aosika


from rest_framework import serializers



# class GoodsSerializer(serializers.Serializer):
    # name = serializers.CharField(required=True, max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()



from goods.models import Goods,GoodsCategory

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)   # 在前端的2及类目包含3级类目
    class Meta:
        model = GoodsCategory
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):
    # 因为商品类别中有三级，GoodsCategory类以自身作为外键，一级是二级的外键，二级是三级的外键
    # 可以用如下方式在前段显示外键
    sub_cat = CategorySerializer2(many=True)   # 注：sub_cat与model中GoodsCategory中的related_name一样
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name','click_num','market_price','add_time')
        fields = "__all__"


