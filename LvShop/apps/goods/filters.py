#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/27 15:42 
# @Author : aosika

#  https://github.com/carltongibson/django-filter   github地址
import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    price_min = django_filters.NumberFilter(name='shop_price',lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price',lookup_expr='lte')
    name = django_filters.CharFilter(name='name',lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))
        #category_id：商品的父类别（3级类目），category__parent_category_id：商品的父类别的父类别（2级类目）
    class Meta:
        model = Goods
        fields = ['price_min','price_max','name']
