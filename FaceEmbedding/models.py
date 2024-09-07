from django.db import models


# Model to store face embedding data, including age, emotion, gender, and timestamp.
class FaceEmbed(models.Model):
    age = models.IntegerField()
    emotion = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
