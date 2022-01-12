from django.db import models
from django.db.models.deletion import CASCADE

class Topic(models.Model):
  short_desc = models.CharField(max_length=30)
  long_desc = models.CharField(max_length=200)
  def __str__(self):
    return self.short_desc+" - "+self.long_desc

class Folder(models.Model):
  name = models.CharField(max_length=30)
  topics = models.ManyToManyField(Topic)
  def __str__(self):
    return self.name

class Document(models.Model):
  folder = models.ForeignKey(Folder, on_delete=CASCADE)
  title = models.CharField(max_length=30)
  content = models.CharField(max_length=200)
  topics = models.ManyToManyField(Topic)
  def __str__(self):
    return self.folder+"/"+self.title