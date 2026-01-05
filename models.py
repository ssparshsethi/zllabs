from django.db import models
# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField()
    image=models.ImageField(upload_to='media/', blank=True, null=True)
    date= models.DateField()


    def __str__(self):
        return self.name

class Customer(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    pdf = models.FileField(upload_to='media/', blank=True, null=True)
    meeting = models.URLField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.title
class Image(models.Model):
    image = models.ImageField(upload_to='media/', blank=True, null=True)

class Logo(models.Model):
    logo = models.ImageField(upload_to='media/', blank=True, null=True)


class Review(models.Model):

    name=models.CharField(max_length=30)
    message=models.TextField(max_length=200)
    image=models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name    

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.username


