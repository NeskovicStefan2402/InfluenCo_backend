from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
import json
from datetime import datetime
from django.forms.models import model_to_dict
from influencer.models import Influencer
from company.models import Company
from .models import Chat,Message,MessageFile

def get_all_chats_for_influencer(id):
    influencer = Influencer.objects.get(id = id)
    chats = Chat.objects.filter(influencer = influencer)
    lista=[{'id_chat':i.id,'id':i.company.id,'name':i.company.name,'image':str(i.company.logo),'seen':True if len(Message.objects.filter(chat = i,sendCompany=True))==0 else  Message.objects.filter(chat = i,sendCompany=True).order_by('-created')[0].seen} for i in chats]
    return HttpResponse(json.dumps(lista),content_type='application/json',status=200)

def get_all_chats_for_company(id):
    company = Company.objects.get(id = id)
    chats = Chat.objects.filter(company = company)
    lista=[{'id_chat':i.id,'id':i.influencer.id,'name':i.influencer.first_name+' '+i.influencer.last_name,'image':str(i.influencer.image),'seen':True if len(Message.objects.filter(chat = i,sendInfluencer=True))==0 else  Message.objects.filter(chat = i,sendInfluencer=True).order_by('-created')[0].seen} for i in chats]
    return HttpResponse(json.dumps(lista),content_type='application/json',status=200)

def get_all_chats(request,type,id):
    if request.method == 'GET':
        if type == 'company':
            return get_all_chats_for_company(id)
        elif type == 'influencer':
            return get_all_chats_for_influencer(id)
        else:
            return HttpResponse({'Error':'Unknown request!'},content_type='application/json',status=404)

def get_messages_for_chat(request,id):
    if request.method == 'GET':
        return get_messages(id)

def get_messages(id):
    chat = Chat.objects.get(id = id)
    messages = Message.objects.filter(chat = chat)
    lista=[{'id':i.pk,'text':i.text,'seen':i.seen,'sendCompany':i.sendCompany,'sendInfluencer':i.sendInfluencer,'datetime':str(i.created)} for i in messages]
    for i in lista:
        message = Message.objects.get(id=i['id'])
        files=MessageFile.objects.filter(message= message)
        files_list=[{'name':j.file} for j in files]
        i['files']=files_list
    return HttpResponse(json.dumps(lista),content_type='application/json',status=200)

def post_message(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        influencer = Influencer.objects.get(id = body['id_influencer'])
        company = Company.objects.get(id = body['id_company'])
        try:
            chat = Chat.objects.get(id = body['id_chats'])
        except:
            chat = Chat.objects.create(influencer = influencer, company = company)
        sendInfluencer = True if body['send']== 'influencer' else False  
        sendCompany = False if body['send']== 'influencer' else True  
        
        messages = Message.objects.filter(chat = chat,sendInfluencer=sendCompany)
        if len(messages):
            print(messages.order_by('-created')[0].text)
            messages.order_by('-created')[0].seen = True
            messages.order_by('-created')[0].save()
        message = Message.objects.create(chat = chat , created = datetime.now(), text = body['text'],sendInfluencer = sendInfluencer,sendCompany = sendCompany)
        return get_messages(chat.id)