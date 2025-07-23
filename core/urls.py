from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ecommerce.urls')),

    # Swagger
    path(
        "api/swagger/schema/", SpectacularAPIView.as_view(), name="schema"
    ),  # Gera o schema OpenAPI em YAML/JSON
    path(
        "api/swagger/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),  # Swagger UI
    path(
        "api/swagger/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),  # Redoc
]
