from .models import FileMetadata
from .serializers import FileMetadataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class FileMetadataCrudViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FileMetadata.objects.all()
    serializer_class = FileMetadataSerializer