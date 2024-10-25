from django_filters.rest_framework import FilterSet
from django_filters import filters
from django_filters import rest_framework as filters
from base.models import UserBaseModel
class BaseUserFitter(filters.FilterSet):
  phone = filters.CharFilter(field_name='phone', lookup_expr="icontains")
  class Meta:
    model = UserBaseModel
    fields = ('phone',)
