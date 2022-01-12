from rest_framework import serializers
from documents.models import Topic, Folder, Document
import logging

logger = logging.getLogger(__name__)

class TopicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topic
    fields = ['id', 'short_desc', 'long_desc']

class FolderSerializer(serializers.ModelSerializer):
  topics = TopicSerializer(many=True, read_only=True)
  class Meta:
    model = Folder
    fields = ['id', 'name', 'topics']

class DocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Document
    fields = ['id', 'title', 'content', 'folder', 'topics']

  def to_representation(self, instance):
      ret = super().to_representation(instance)
      ret['folder'] = FolderSerializer(instance.folder).data
      ret['topics'] = []
      for topic in instance.topics.all():
        ret['topics'].append(TopicSerializer(topic).data)
      return ret
  
  def create(self, validated_data):
        topic_ids = validated_data.pop('topics')
        document = Document.objects.create(**validated_data)
        document.topics.set(topic_ids)
        return document