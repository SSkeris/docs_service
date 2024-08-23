from rest_framework.routers import DefaultRouter

from docs.apps import DocsConfig
from docs.views import DocumentViewSet

app_name = DocsConfig.name
router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='docs')

urlpatterns = [] + router.urls
