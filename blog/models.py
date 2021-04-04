from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
