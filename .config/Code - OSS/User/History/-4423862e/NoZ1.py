from django.shortcuts import render
from .serializers import QuoteSerializer,CommentSerializer
from .models import Quote,Comment
from rest_framework.views import APIView
from rest_framework.response import Response

class QuoteViewSet(APIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class CommentViewSet(APIView):
    def get(self,req):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments,many=True)
        return Response (serializer.data)