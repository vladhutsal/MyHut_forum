from django import forms
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

# organize by tags
# recent Topics
# search by title
# reccomend this topic? rating of topics

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    tags = models.ManyToManyField('Tag', blank=True)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{} ({})'.format(self.title, self.user)
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return 'comment: {}, user: {}, topic: {}'.format(self.text, self.user, self.topic)
    
   
class RelatedComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
