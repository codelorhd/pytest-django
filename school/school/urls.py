from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include, re_path
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('classroom.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token)

]
