from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from page.views import RedirectToAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor", include("ckeditor_uploader.urls")),
    path("api/", include('api.urls', namespace="api")),
    path("", RedirectToAdmin.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)