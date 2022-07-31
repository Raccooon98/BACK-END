from urllib.request import parse_http_list
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    # path('account/login/callback/', ),
]
