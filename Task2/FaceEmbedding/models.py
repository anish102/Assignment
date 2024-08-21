from django.db import models


class FaceEmbed(models.Model):
    age = models.IntegerField()
    emotion = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
