from django.db import models
import uuid

class FileMetadata(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    format = models.CharField(max_length=5)
    size = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename()
    
    def filename(self):
        return self.name + "." + self.format
