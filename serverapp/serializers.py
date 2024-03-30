from rest_framework.serializers import ModelSerializer
from .models import *
class MountainsSerializer(ModelSerializer):
    class Meta:
        model = Mountains
        fields = (
            'mountain_id', 'mountain_name', 'description', 'image_path', 'image_source'
        )

