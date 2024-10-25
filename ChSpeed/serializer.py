from enum import Enum
from rest_framework.serializers import ModelSerializer,ListSerializer,BaseSerializer
from rest_framework.fields import empty
class DisplayType(Enum):
    LIST = "LIST"
    FOREIGN = "FOREIGN"
    DETAIL = "DETAIL"
class BaseSerializer(ModelSerializer):

  # 展示类型
  display_type = None
  # 敏感字段，不会被序列化
  sensitive_fields = []
  # 标记作为外键时引用需要排除的字段
  exclude_foreign = []
  # 标记作为列表展示时需要排除的字段
  exclude_list = []

  def __init__(self,instance=None,data=empty, **kwargs):
    super().__init__(instance=instance,data=data, **kwargs)

    if isinstance(instance,list) and self.display_type==None:
      self.display_type = DisplayType.LIST

    for field_name in self.sensitive_fields:
      self.fields.pop(field_name)
    if self.display_type == DisplayType.LIST:
      self._remove_fields(self.exclude_list)
    if self.display_type == DisplayType.FOREIGN:
      self._remove_fields(self.exclude_list)



  def _remove_fields(self, field_names):
    """移除字段的方法"""
    for field_name in field_names:
      self.fields.pop(field_name, None)
