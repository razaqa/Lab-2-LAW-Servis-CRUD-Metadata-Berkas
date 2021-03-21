from rest_framework import routers
from .views import FileMetadataCrudViewSet

router = routers.DefaultRouter()
router.register(r'metadata', FileMetadataCrudViewSet)