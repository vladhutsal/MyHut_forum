from django.db import models
from login.models import User


# organize by tags
# recent Topics
# search by title
# reccomend this topic? rating of topics


class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-pk']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_like')

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return 'User: {}, Topic: {}'.format(self.user, self.topic)
