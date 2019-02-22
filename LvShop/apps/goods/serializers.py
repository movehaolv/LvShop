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
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name','click_num','market_price','add_time')
        fields = "__all__"


