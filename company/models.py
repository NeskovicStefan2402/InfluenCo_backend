from django.db import models
from influencer import models as influencer_models
class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to ='companies/')
    desription = models.TextField()
    idNumber = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    type = models.ForeignKey('TypeCompany',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class TypeCompany(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='jobs/')
    description = models.TextField()
    price = models.FloatField()
    company = models.ForeignKey('Company',on_delete=models.SET_NULL,null=True)
    selected = models.ForeignKey('influencer.Influencer',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name

class Interests_for_job(models.Model):
    job = models.ForeignKey('Job',on_delete=models.SET_NULL,null=True)
    influencer = models.ForeignKey('influencer.Influencer',on_delete=models.SET_NULL,null=True,blank = True)

    def __str__(self):
        return self.job.name+'  -  '+self.influencer.first_name+' '+self.influencer.last_name

