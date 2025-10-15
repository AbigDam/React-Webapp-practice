from django.contrib import admin
from django.urls import path, include
from scheduler.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("scheduler/user/register/", CreateUserView.as_view(), name="register"),
    path("scheduler/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("scheduler/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("scheduler-auth/", include("rest_framework.urls")),
    #path("scheduler/", include("scheduler.urls")),
]