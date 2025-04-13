from rest_framework import serializers
from .models import EducationResource

class EducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationResource
        fields= ['id', 'title', 'url', 'description', 'disease', 'resource_type', 'tags', 'created_at']