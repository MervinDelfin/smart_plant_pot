from django.db import models

# Create your models here.
class State(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    moisture = models.IntegerField()

    def __str__(self):
        return self.date + " " + self.moisture