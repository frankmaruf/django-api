from django.urls import path
from rest_framework.decorators import api_view
from .views import (article_list,
article_detail,
ArticleAPIView,
ArticalDetails,
GenericAPIView,
ArticleViewSet,
ArticleSimpleViewSet,
ArticleSimpleModelViewSet
)



urlpatterns = [
    # path('article', article_list),
    path('article',ArticleAPIView.as_view()),
    path('generic/article',GenericAPIView.as_view()),
    path('generic/article/<str:pk>',GenericAPIView.as_view()),

    path('simple_model_viewset/atricle',ArticleSimpleModelViewSet.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path('simple_model_viewset/atricle/<str:pk>',ArticleSimpleModelViewSet.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),









    path('simple_viewset/atricle',ArticleSimpleViewSet.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path('simple_viewset/atricle/<str:pk>',ArticleSimpleViewSet.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),




    path('viewset/article',ArticleViewSet.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path('viewset/article/<str:pk>',ArticleViewSet.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
    # path('article/<str:pk>',article_detail)
    path('article/<str:id>',ArticalDetails.as_view())
]