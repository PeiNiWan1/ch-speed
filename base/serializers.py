
from base.models import UserBaseModel
from rest_framework.serializers import Serializer,CharField,ModelSerializer
from django.contrib.auth.hashers import make_password
class UserSerializer(ModelSerializer):
  phone = CharField(required=True)

  class Meta:
    model = UserBaseModel
    fields = '__all__'

  def create(self, validated_data):
    # 如果没有密码，则默认密码为手机号
    if 'password' not in validated_data:
      validated_data['password'] = make_password(validated_data['phone'])

    return super().create(validated_data)
