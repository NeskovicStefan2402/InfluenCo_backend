from django.db import models
from influencer import models as influencer_models
from company import models as company_models

class Chat(models.Model):
    influencer = models.ForeignKey('influencer.Influencer',on_delete=models.SET_NULL,null=True)
    company = models.ForeignKey('company.Company',on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return str(self.influencer) + ' : ' + str(self.company) + ' ======> '+ str(self.pk)

class Message(models.Model):
    chat = models.ForeignKey('Chat',on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField()
    sendInfluencer = models.BooleanField(default=False)
    sendCompany = models.BooleanField(default=False)
    text = models.TextField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return str(self.chat) + ' - ' + str(self.text)

class MessageFile(models.Model):
    message = models.ForeignKey('Message',on_delete=models.SET_NULL,null=True)
    file = models.FileField(upload_to='files/')
    
    def __str__(self):
        return str(self.message) + ' -- file'

