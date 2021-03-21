from rest_framework.viewsets import ModelViewSet
from .serializer import FileMetadataSerializer
from .models import FileMetadata

class FileMetadataCrudViewSet(ModelViewSet):
    queryset = FileMetadata.objects.all()
    serializer_class = FileMetadataSerializer