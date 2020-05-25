from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Vendor.models import Menu
from .serializers import MenuSerializer


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Menu.objects.all()
        serializer = MenuSerializer(snippets, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = MenuSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)