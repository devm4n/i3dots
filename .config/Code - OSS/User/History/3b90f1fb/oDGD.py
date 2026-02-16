from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.views import APIView

class SnippetViewAPI(APIView):

    def get(self,request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)