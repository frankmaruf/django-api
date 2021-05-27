from django.urls import path
from rest_framework.decorators import api_view
from .views import article_list,article_detail,ArticleAPIView,ArticalDetails


urlpatterns = [
    # path('article', article_list),
    path('article',ArticleAPIView.as_view()),
    # path('article/<str:pk>',article_detail)
    path('article/<str:id>',ArticalDetails.as_view())
]