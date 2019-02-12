#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/10 17:17 
# @Author : aosika


from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()
