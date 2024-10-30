from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import auth
from django.contrib.auth.hashers import make_password

from django.contrib.auth.base_user import BaseUserManager
from django.apps import apps

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone,email, password, **extra_fields):
        email = self.normalize_email(email)
        print("创建用户",email,password,phone,extra_fields)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.username = phone
        user.password =make_password(password)
        user.save(using=self._db)
        print("创建用户",user,password,make_password(password))
        return user

    def create_user(self,  email=None, password=None,phone=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, phone=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class UserBaseModel(AbstractUser):
    phone = models.CharField("phone",max_length=11, null=False, blank=True,unique=True)
    username = models.CharField("username",max_length=32,null=False, blank=True)
    email=None
    objects = UserManager()
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS =[]

    class Meta:
        db_table = "user_base"

    def __str__(self):

        return self.phone



    def get_class_name(self):
        return self.__class__.__name__
