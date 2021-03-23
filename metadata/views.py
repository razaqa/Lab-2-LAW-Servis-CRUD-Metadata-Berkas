from .models import FileMetadata
from .serializers import FileMetadataSerializer
from rest_framework.viewsets import ModelViewSet

class FileMetadataCrudViewSet(ModelViewSet):
    queryset = FileMetadata.objects.all()
    serializer_class = FileMetadataSerializer