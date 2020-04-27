from django.shortcuts import render
from influencer.models import Influencer
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
from .models import Company,Job,Interests_for_job,TypeCompany
from .other import default_image
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

def postCompanyLogo(request,id):
    if request.method=='POST':
        print(request.FILES['image'])
        company=Company.objects.get(id=id)
        company.logo=request.FILES['image']
        company.save()
        return HttpResponse(serialize('json',[company]),content_type='application/json',status=200)

def postJobImage(request,id):
    if request.method=='POST':
        print(request.FILES['image'])
        job=Job.objects.get(id=id)
        job.image=request.FILES['image']
        job.save()
        return HttpResponse(serialize('json',[job]),content_type='application/json',status=200)

def signUpCompany(request):
    if request.method=='POST':
        body_u=request.body.decode('utf-8')
        body=json.loads(body_u)
        company=Company.objects.filter(idNumber = body['idNumber']).first()
        if company:
            return HttpResponse({'Error':'This company already exist!'},content_type='application/json',status=401)
        else:
            default_image(body['name'])
            type = TypeCompany.objects.get(id=body['type'])
            company=Company.objects.create(name=body['name'] , idNumber=body['idNumber'], desription = body['description'], password = body['password'] , type = type ,logo='companies/'+str(body['name']).replace('.','')+'.jpg') 
            return HttpResponse(serialize('json',[company]),content_type='application/json',status=200)

def postJob(request):
    if request.method=='POST':
        body_u=request.body.decode('utf-8')
        body=json.loads(body_u)
        # try:
        company=Company.objects.get(id=body['company'])
        job_int=Job.objects.filter(name=body['name']).first()
        if job_int:
            return HttpResponse({'Error':'This job already exist!'},content_type='application/json',status=401)
        else:
            job=Job.objects.create(name=body['name'],description=body['description'],price=body['price'],company=company,selected=None)
            return HttpResponse(serialize('json',[job]),content_type='application/json',status=200)
        # except Exception as e:
        #     return HttpResponse({'Error':str(e)},content_type='application/json',status=401)

def updateJob(request):
    if request.method=='POST':
        body_unicode=request.body.decode('utf-8')
        body=json.loads(body_unicode)
        job = Job.objects.get(id = body['id'])
        if job:
            job.name = body['name']
            job.description = body['description']
            job.price = body['price']
            job.save()
            return HttpResponse(serialize('json',[job]),content_type='application/json',status=200)
        else:
            return httpResponse({'Error':'Job dont exist!'},content_type='application/json',status=400)

def deleteJob(request,id):
    if request.method == 'POST':
        job = Job.objects.get(id=id)
        if job:
            job.delete()
            return HttpResponse({'Success':'Successfully delete job!'},content_type='application/json',status=200)
        else:
            return HttpResponse({'Error':'Job dont exist!'},content_type='application/json',status=400)

def get_influencers_for_active_job(request,id):
    if request.method == 'GET':
        lista = []
        for i in Interests_for_job.objects.all():
            if i.job.id == id:
                lista.append(i.influencer)
        print(lista)  
        return  HttpResponse(serialize('json',lista),content_type='spplication/json',status=200)

def finish_job(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body=json.loads(body_unicode)
        job = Job.objects.get(id=body['id'])
        influencer = Influencer.objects.get(id = body['influencer'])
        job.selected = influencer
        job.save()
        return HttpResponse({'Success':'This job is finished!'},content_type='application/json',status=200)