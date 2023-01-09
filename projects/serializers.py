from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= ('id', 'title', 'description', 'technology', 'creation_date')
        #Recordar poner la coma al final, de esta forma, python reconoce que es una tupla,
        #en el caso contrario, lo lee como string.
        read_only_fields=('creation_date',) 