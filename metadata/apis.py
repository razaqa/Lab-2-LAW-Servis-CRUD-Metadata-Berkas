from .views import FileMetadataCrudViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'metadata', FileMetadataCrudViewSet)