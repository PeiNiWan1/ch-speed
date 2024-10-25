from django.db import models
class BaseModel(models.Model):

  def get_class_name(self):
    return None
