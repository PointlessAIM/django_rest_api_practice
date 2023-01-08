from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= ('id', 'title', 'description', 'technology', 'creation_date')
        read_only_fields=('creation_date')