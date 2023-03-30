from django.db import models

# Create your models here.
class State(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    moisture = models.IntegerField()

    def __str__(self):
        return str(self.date) + " - " + str(self.moisture) + "%"
    
class DefindedState(models.Model):
    name = models.CharField(max_length=255)
    moisture = models.IntegerField()

    def __str__(self):
        return self.name + ": " + str(self.moisture) + "%"
    

class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    def __str__(self):
        return str(self.date) + " - " + self.message
