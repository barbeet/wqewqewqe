from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('general_apteka.urls')),
    path('accounts/', include('users.urls')),
    path('summernote/', include('django_summernote.urls')),
 	path('api/', include("api_apteka.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


