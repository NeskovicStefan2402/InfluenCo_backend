from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
from .models import Company

def getCompanies(request):
    companies=Company.objects.all()
    ser_companies=serialize('json',companies,fields=('name','logo','description','idNumber'))
    return HttpResponse(ser_companies, content_type='application/json')


