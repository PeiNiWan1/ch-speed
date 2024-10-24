
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from base.views import UserView,LoginView
from knox import views as knox_views
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # 自定义的登录视图
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserView)

urlpatterns += router.urls
