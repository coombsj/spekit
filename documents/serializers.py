from typing_extensions import Required
from rest_framework import serializers
from documents.models import Topic, Folder, Document

class TopicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topic
    fields = ['id', 'short_desc', 'long_desc']

class FolderSerializer(serializers.HyperlinkedModelSerializer):
  topics = serializers.HyperlinkedIdentityField(many=True, view_name='topic-detail', read_only=True)
  class Meta:
    model = Folder
    fields = ['id', 'name', 'topics']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
  topics = serializers.HyperlinkedRelatedField(many=True, view_name='topic-detail', read_only=True)
  folder = serializers.HyperlinkedIdentityField(view_name='folder-detail')
  class Meta:
    model = Document
    fields = ['id', 'title', 'content', 'folder', 'topics']
  