from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from models import Snippet
from .serializers import SnippetSerializer
from rest_framework.views import APIView

class SnippetViewAPI(APIView):
    def get(self,request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(data=snippets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)