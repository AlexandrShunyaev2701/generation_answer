from django.db import models


class Answer(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title
