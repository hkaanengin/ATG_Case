from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import iatacodes
from . serializers import iataSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class iataapi(APIView):

    #def get(self,request):
        #kek=iatacodes.objects.filter(iata="TK")
        #serializer=iataSerializer(kek,many=True)
        #return Response(serializer.data)
    
    @permission_classes((IsAuthenticated,))
    def  post(self,request, *args,**kwargs):
        iata_code=request.data["iata"]
        filtered_iata=iatacodes.objects.filter(iata=iata_code)
        serializer=iataSerializer(filtered_iata,many=True)
        return Response(serializer.data)