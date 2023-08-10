from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=240)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=240)
    desc=models.TextField()

    def __str__(self):
        return self.name