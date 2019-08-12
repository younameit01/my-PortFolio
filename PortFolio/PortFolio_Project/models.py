from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    language = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

    def __str__(self):
        return self.name
