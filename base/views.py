# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions

from django.shortcuts import render
from rest_framework import generics

from models import Dream
from serializer import DreamSerializer
# Create your views here.


class BucketListApi(generics.ListCreateAPIView):
    """To list all dreams"""
    query_set = Dream.objects.all()
    serializer = DreamSerializer
