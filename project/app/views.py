from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status
from app.models import Attachment
from .serializers import UploadAttachment
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class Fileupload(ViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Attachment.objects.all()
        serializer = UploadAttachment(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UploadAttachment(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


