from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    path('api/', include('core.urls')),
    path('api/', include('student.urls')),
    path('api/', include('school.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)