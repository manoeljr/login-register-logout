from django.contrib import admin
from django.urls import path
from auth import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


app_name = 'api'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', views.TokenRefreshView.as_views(), name="token_refresh"),

    path('admin/', admin.site.urls),
]
