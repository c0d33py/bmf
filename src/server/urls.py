from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("robots.txt",
         TemplateView.as_view(template_name="web/robots.txt",
                              content_type="text/plain"),),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
