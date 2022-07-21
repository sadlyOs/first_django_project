from django.db import models


class Project2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    data = models.DateField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
