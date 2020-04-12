from django.db import models

class Influencer(models.Model):
    image = models.ImageField(upload_to ='uploads/')
    instagram = models.CharField(max_length=50)
    instagram_followers=models.IntegerField()
    facebook = models.CharField(max_length=50)
    facebook_likes=models.IntegerField()
    youtube = models.CharField(max_length=50)
    youtube_subscribers=models.IntegerField()
    twitter = models.CharField(max_length=50)
    twitter_followers=models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    age = models.IntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    interest = models.ForeignKey('Interest',on_delete=models.SET_NULL,null=True)
    level = models.ForeignKey('Level',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Level(models.Model):
    name = models.CharField(max_length=20)  
    min = models.IntegerField()
    max = models.IntegerField()

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

class Post(models.Model):
    image=models.ImageField(upload_to='post/')
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

