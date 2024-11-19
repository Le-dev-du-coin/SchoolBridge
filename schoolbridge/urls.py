from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    path('api/', include('core.urls')),
    path('api/', include('student.urls')),
    path('api/', include('school.urls')),
    path('admin/', admin.site.urls),
]
