from django.contrib.auth import get_user_model
from ChSpeed.viewsets import CommonViewSetModel
from base.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from knox.models import AuthToken
from ChSpeed.loggers import Loggers
from base.fitter import BaseUserFitter
from django.contrib.auth.hashers import make_password
class UserView(CommonViewSetModel):
    queryset = get_user_model().objects.all()
    serializer_class=UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_class=BaseUserFitter
    classes_map = {

        # 'list':{'permissions':[],'serializer':None},
        # 'retrieve':{'permissions':[],'serializer':None},
        # 'create':{'permissions':[],'serializer':None},
        # 'update':{'permissions':[],'serializer':None},
        # 'partial_update':{'permissions':[],'serializer':None},
        # 'destroy':{'permissions':[],'serializer':None},
    }
    @action(detail=False,methods=['post'])
    def getMyInfo(self,request):
        print(request.user)
        return Response({"user":"awdawdaw"})
    # 修改密码
    @action(detail=False,methods=['post'])
    def changePassword(self,request):
        user = request.user
        newpassword = request.data.get('newPassword')
        oldpassword = request.data.get('oldPassword')
        if not user.check_password(oldpassword):
            return Response({"msg":"原密码错误","code":4004})
        user.set_password(newpassword)
        user.save()
        return Response({"msg":"修改密码成功"})
class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_model().objects.filter(phone=serializer.data['phone']).first()
        if not user:
            Loggers.info(serializer.data['phone'],"用户不存在")
            return Response({"msg":"用户不存在","code":4004})
        if not user.check_password(serializer.data['password']):
            Loggers.info(serializer.data['phone'],"密码错误")
            return Response({"msg":"密码错误","code":4004})
        if not user.is_active:
            Loggers.info(serializer.data['phone'],"用户被禁用")
            return Response({"msg":"用户被禁用","code":4004})
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": self.get_serializer(user).data,
            "token": token
        })
