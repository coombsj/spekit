from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.api_root),
    path('topics/', views.TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>/', views.TopicDetail.as_view(), name='topic-detail'),
    path('folders/', views.FolderList.as_view(), name='folder-list'),
    path('folders/<int:pk>/', views.FolderDetail.as_view(), name='folder-detail'),
    path('documents/', views.DocumentList.as_view(), name='document-list'),
    path('documents/<int:pk>/', views.DocumentDetail.as_view(), name='document-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)