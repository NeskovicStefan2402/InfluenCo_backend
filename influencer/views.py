from django.shortcuts import render
from django.conf import settings
from .other import facebookImage
import json
from django.http import JsonResponse,HttpResponse,HttpResponseNotFound
from django.core.serializers import serialize
from django.conf.urls.static import static
from django.conf import settings
from .models import Influencer,Interest,Level

def getInfluencers(request):
    influencers=Influencer.objects.all()
    datas=serialize('json',influencers,fields=('first_name','last_name','age','interest','level','image'))
    return HttpResponse(datas,content_type='application/json')
    # return JsonResponse(datas,safe=False)

def getImage(request):
    data=Influencer.objects.get(id=1)
    return render(request,'gallery.html',{"image":'cocaCola.jpg', 'media_url':settings.MEDIA_URL})


def login(request):
    if request.method=='POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email_data=body['email']
        password_data=body['password']
        influencer=Influencer.objects.filter(email=email_data).first()
        if influencer :
            serialize_influencer=serialize('json',[influencer])
            if influencer.password==password_data:
                return HttpResponse(serialize_influencer,content_type='application/json')
            else:
                return JsonResponse({'Error':'Incorrect password field!'})
        else:
            return JsonResponse({'Error':'No regognize profile!'})
    else:
       return HttpResponseNotFound('<h1>Page not found</h1>')
    
def signUp(request):
    if request.method=='POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            interest=Interest.objects.get(id=body['interest'])
            level=Level.objects.filter(name='Beginner').first()
            influencer=Influencer.objects.filter(email=body['email']).first()
            if influencer:
                raise Exception('This profile exist!')
            else:
                image=facebookImage(body['facebook'],body['email'])
                Influencer.objects.create(first_name=body['first_name'],last_name=body['last_name'],email=body['email'],age=body['age'],interest=interest,level=level,youtube=body['youtube'],facebook=body['facebook'],instagram=body['instagram'],twitter=body['twitter'],password=body['password'],facebook_likes=0,youtube_subscribers=0,instagram_followers=0,twitter_followers=0,image='uploads/'+body['email'].replace('.','')+'.jpg') 
                return JsonResponse({'Message':'Correct insert!'},status=200)
        except Exception as e:
            print(str(e))
            return JsonResponse({'Message':'Incorrect insert, because: '+str(e)}) 
    else:
       return HttpResponseNotFound('<h1>Page not found</h1>')
