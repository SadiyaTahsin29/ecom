from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# DRF Spectacular (API Schema and Documentation)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# DRF-yasg (Swagger Documentation)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# JWT Authentication Views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def home(request):
    return HttpResponse("Welcome to the E-Commerce API!")


# DRF-yasg Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
        description="API documentation for the ecommerce project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL Patterns
urlpatterns = [
    # Root URL (Homepage)
    path("", home, name="home"),  # Handles requests to `/`

    # Admin Panel
    path("admin/", admin.site.urls, name="admin"),

    # E-commerce app URLs
    # Ensure namespace matches
    path('sassique/', include('sassique.urls', namespace='sassique')),

    # Authentication Endpoints (JWT)
    path("api/auth/token/", TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("api/auth/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),

    # Include allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # DRF Spectacular Schema and Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/",
         SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/",
         SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # DRF-yasg Swagger Documentation
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]

# Serve Media Files During Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
