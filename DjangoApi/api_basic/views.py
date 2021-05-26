from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleModelSerializer
# Create your views here.
