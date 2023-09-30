from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pictures')
    disc = models.TextField()

    def __str__(self):
        return self.name



class People(models.Model):
    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pic')
    des = models.TextField()


    def __str__(self):
        return self.name1