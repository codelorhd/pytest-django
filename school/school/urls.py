from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('classroom.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))

]
