from django.test import TestCase
from django.urls import reverse
from documents.models import Topic

def create_topic(short_desc, long_desc):
    return Topic.objects.create(short_desc=short_desc, long_desc=long_desc)

class TopicDetailViewTests(TestCase):
    def test_no_topics_defined(self):
        url = reverse('topic-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "[]")
    
    def test_topic_list(self):
      topic = create_topic(short_desc="Topic 1", long_desc="This is topic 1")
      url = reverse('topic-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, 200)
      self.assertQuerysetEqual('', [topic])
