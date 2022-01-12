from documents.models import Topic, Folder, Document
from documents.serializers import TopicSerializer, FolderSerializer, DocumentSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'documents': reverse('document-list', request=request, format=format),
        'folders': reverse('folder-list', request=request, format=format),
        'topics': reverse('topic-list', request=request, format=format)
    })

class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class FolderList(generics.ListCreateAPIView):
    # queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    
    def get_queryset(self):
        queryset = Folder.objects.all()
        topic_id = self.request.query_params.get('topic_id')
        if topic_id is not None:
            queryset = queryset.filter(topics__pk=topic_id)
        return queryset

class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class DocumentList(generics.ListCreateAPIView):
    # queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        topic_id = self.request.query_params.get('topic_id')
        if topic_id is not None:
            queryset = queryset.filter(topics__pk=topic_id)
        folder_topic_id = self.request.query_params.get('folder_topic_id')
        if folder_topic_id is not None:
            folder_queryset = Folder.objects.all()
            folder_queryset = folder_queryset.filter(topics_pk=folder_topic_id)
            queryset = queryset.filter
        folder_id = self.request.query_params.get('folder_id')
        if folder_id is not None:
            queryset = queryset.filter(folder__pk=folder_id)
        
        return queryset

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer