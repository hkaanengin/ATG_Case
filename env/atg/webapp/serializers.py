from rest_framework import serializers
from . models import iatacodes

class iataSerializer(serializers.ModelSerializer):

    class Meta:
        model=iatacodes
        #fields=('firstname','lastname')
        fields='__all__'