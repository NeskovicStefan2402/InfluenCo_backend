from django.shortcuts import render
from influencer.models import Influencer
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
from .models import Company,Job,Interests_for_job,TypeCompany
import json

def getCompanies(request):
    companies=Company.objects.all()
    ser_companies=serialize('json',companies)
    return HttpResponse(ser_companies, content_type='application/json')

def get_active_jobs(request):
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    if request.method=='GET':
        jobs=Job.objects.filter(selected=None)
        serialize_jobs=serialize('json',jobs)
        return HttpResponse(serialize_jobs,content_type='application/json')

def set_interest_for_job(request):
    if request.method=='POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        interest=Interests_for_job.objects.filter(job=body['job']).filter(influencer=body['influencer']).first()
        if interest:
            interest.delete()
            # return HttpResponse({'Error':'Influencer selected interest for that job!'},status=401)
        else:
            influencer=Influencer.objects.get(id=body['influencer'])
            job=Job.objects.get(id=body['job'])
            interest=Interests_for_job.objects.create(job=job,influencer=influencer)
            # serialize_interest=serialize('json',[interest])
        influencer=Influencer.objects.get(id=body['influencer'])
        interests=Interests_for_job.objects.filter(influencer=influencer)
        lista=[]
        for i in interests:
            ser=json.loads(serialize("json", [i]))
            job=Job.objects.get(id=ser[0]['fields']['job'])
            lista.append(job)
        serialize_interests=serialize('json',lista)
        return HttpResponse(serialize_interests,content_type='application/json',status=200)    

def get_interests_for_influencer(request,id):
    if request.method=='GET':
        influencer=Influencer.objects.get(id=id)
        interests=Interests_for_job.objects.filter(influencer=influencer)
        lista=[]
        for i in interests:
            ser=json.loads(serialize("json", [i]))
            job=Job.objects.get(id=ser[0]['fields']['job'])
            lista.append(job)
        serialize_interests=serialize('json',lista)
        return HttpResponse(serialize_interests,content_type='application/json')
        
def get_types(request):
    if request.method=='GET':
        types=TypeCompany.objects.all()
        serialize_types=serialize('json',types)
        return HttpResponse(serialize_types,content_type='application/json')
