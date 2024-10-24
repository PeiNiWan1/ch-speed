from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter
from base.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from knox.models import AuthToken
from ChSpeed.loggers import Loggers

class UserView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class=UserSerializer
    filter_backends = [SearchFilter]
    search_fields=['phone','username']
    permission_classes = [IsAuthenticated]
    @action(detail=False,methods=['post'])
    def getMyInfo(self,request):
        print(request.user)
        return Response({"user":"awdawdaw"})
class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_model().objects.filter(phone=serializer.data['phone']).first()
        if not user:
            Loggers.info(serializer.data['phone'],"用户不存在")
            return Response({"msg":"用户不存在","code":4004})
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": self.get_serializer(user).data,
            "token": token
        })
