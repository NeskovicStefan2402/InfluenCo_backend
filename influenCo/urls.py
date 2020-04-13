"""influenCo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from influencer.views import getInfluencers,getImage,login,signUp,getInterests,uploadImage,updateInfluencer
from company.views import getCompanies,get_active_jobs,set_interest_for_job,get_interests_for_influencer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getInfluencers/',getInfluencers),
    path('getImage/',getImage),
    path('getCompanies/',getCompanies),
    path('loginInfluencer/',csrf_exempt(login)),
    path('signUpInfluencer/',csrf_exempt(signUp)),
    path('getInterests/',getInterests),
    path('uploadImage/',csrf_exempt(uploadImage)),
    path('updateInfluencer/',csrf_exempt(updateInfluencer)),
    path('getActiveJobs/',csrf_exempt(get_active_jobs)),
    path('setInterestForJob/',csrf_exempt(set_interest_for_job)),
    path('getInterestsForInfluencer/<int:id>',csrf_exempt(get_interests_for_influencer))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
