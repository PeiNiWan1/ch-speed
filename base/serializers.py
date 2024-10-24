
from base.models import UserBaseModel
from rest_framework.serializers import Serializer,CharField,ModelSerializer
class UserSerializer(ModelSerializer,Serializer):
  phone = CharField(required=True)
  class Meta:
    model = UserBaseModel
    fields = '__all__'

