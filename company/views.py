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
        else:
            influencer=Influencer.objects.get(id=body['influencer'])
            job=Job.objects.get(id=body['job'])
            interest=Interests_for_job.objects.create(job=job,influencer=influencer)
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

def loginCompany(request):
    if request.method=='POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            company = Company.objects.filter(name=body['name']).first()
            if company:
                if company.password == body['password']:
                    serialize_company = serialize('json', [company])
                    return HttpResponse(serialize_company,content_type='application/json')
                else:
                    return HttpResponse({'error':'Your password is incorrect!'},content_type='application/json',status=401)
            else:
                return HttpResponse({'error':'Name of your company is incorrect!'},content_type='application/json',status=401)
        except Exception as e:
            return HttpResponse({'error':str(e)},content_type='application/json',status=404)

def exist(data,array):
    if data:
        exist=False
        for i in array:
            if i['inf']== data:
                i['jobs']+=1
                exist=True 
        if exist==False:
            array.append({'inf':data,'jobs':1})
    return array
            
def makeList(lista):
    new=[]
    for i in sorted(lista, key = lambda i: i['jobs'],reverse=True):
        new.append(i['inf'])
    # return sorted(new, key = lambda i: i['jobs']) 
    return new

def getPopularInfluencers(request):
    if request.method=='GET':
        jobs=Job.objects.all()
        lista=[]
        for i in jobs:
            lista=exist(i.selected,lista)
        return HttpResponse(serialize('json',makeList(lista)),content_type='application/json')    

def get_jobs_for_company(request,id):
    if request.method=='GET':
        jobs=Job.objects.filter(selected__isnull=False).filter(company=id)
        serialize_jobs=serialize('json',jobs)
        return HttpResponse(serialize_jobs,content_type='application/json')

def updateCompany(request):
    if request.method=='POST':
        body_u=request.body.decode('utf-8')
        body=json.loads(body_u)
        company = Company.objects.get(id=body['id'])
        if company:
            company.name=body['name']
            company.desription=body['desription']
            company.save()
            ser_company=serialize('json',[company])
            return HttpResponse(ser_company, content_type='application/json',status=200)
        else:
           return HttpResponse({'Error':'This company dont exist!'}, content_type='application/json',status=401)
         