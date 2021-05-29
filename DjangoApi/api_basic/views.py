from functools import partial
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleModelSerializer,ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import generics,mixins,status
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.




class ArticleSimpleViewSet(viewsets.GenericViewSet,mixins.DestroyModelMixin, mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    serializer_class = ArticleModelSerializer
    queryset = Article.objects.all()


class ArticleSimpleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleModelSerializer
    queryset = Article.objects.all()


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleModelSerializer(instance=article,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def partial_update(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleModelSerializer(instance=article,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        article = Article.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class GenericAPIView(generics.GenericAPIView,
mixins.ListModelMixin,
mixins.CreateModelMixin,
mixins.UpdateModelMixin,mixins.RetrieveModelMixin,
mixins.DestroyModelMixin):
    serializer_class = ArticleModelSerializer
    queryset = Article.objects.all()
    lookup_field = 'pk'
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None):
        if pk:
            return self.retrieve(request, pk)

        return self.list(request)

    def post(self, request):
        return self.create(request)
    def put(self, request,pk=None):
        return self.partial_update(request,pk)
    def delete(self, request, pk=None):
        return self.destroy(request,pk)







class ArticleAPIView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticalDetails(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleModelSerializer(article, many=False)
        return Response(serializer.data)
    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleModelSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT','DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ArticleModelSerializer(article, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleModelSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)