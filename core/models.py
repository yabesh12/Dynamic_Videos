from django.db import models
from core.utils import generate_vid


class Content(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title)


class Video(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='videos/')
    vid = models.CharField(max_length=250, editable=False, default=generate_vid)

    def __str__(self):
        return str(self.name)


class HtmlContent(models.Model):
    content = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)
