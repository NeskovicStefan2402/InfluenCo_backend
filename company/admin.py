from django.contrib import admin
from .models import TypeCompany,Company,Interests_for_job,Job

admin.site.register(TypeCompany)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Interests_for_job)
