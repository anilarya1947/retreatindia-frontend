from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from blog.api import router as wagtail_api_router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('api/', include('listings.urls')),
    path('api/contact/', include('contact.urls')),
    path('pages/', include(wagtail_urls)),
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v2/', wagtail_api_router.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)