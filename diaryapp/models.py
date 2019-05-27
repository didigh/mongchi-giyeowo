from django.db import models

# Create your models here.

class Diary (models.Model):
    title = models.CharField(max_length = 20)
    image = models.FileField(upload_to='images/')
    # image = models.ImageField(upload_to='images/')
    body = models.TextField()
    date = models.DateTimeField('date published')

    def sum(self):
        return self.body[:10]






