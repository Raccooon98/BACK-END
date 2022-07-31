from urllib.request import parse_http_list
from django.contrib import admin
from django.urls import path,include
from .views import kakaoGetLogin, getUserInfo
urlpatterns = [
    path('login/', kakaoGetLogin),
    path('login/callback/', getUserInfo, name="kakao_callback"),
]
