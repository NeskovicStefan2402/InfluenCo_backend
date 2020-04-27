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
from influencer.views import getInfluencers,loginInfluencer,signUp,getInterests,updateInfluencer,postInfluencerImage
from company.views import getCompanies,get_active_jobs,set_interest_for_job,get_interests_for_influencer,get_types,loginCompany,getPopularInfluencers,get_jobs_for_company,updateCompany,postJob,postCompanyLogo,postJobImage
from company.views import signUpCompany,updateJob,deleteJob,get_influencers_for_active_job,finish_job
from chat.views import get_all_chats,get_messages_for_chat,post_message
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getInfluencers/',getInfluencers),
    path('getCompanies/',getCompanies),
    path('loginInfluencer/',csrf_exempt(loginInfluencer)),
    path('signUpInfluencer/',csrf_exempt(signUp)),
    path('getInterests/',getInterests),
    path('updateInfluencer/',csrf_exempt(updateInfluencer)),
    path('getActiveJobs/',csrf_exempt(get_active_jobs)),
    path('setInterestForJob/',csrf_exempt(set_interest_for_job)),
    path('getInterestsForInfluencer/<int:id>',csrf_exempt(get_interests_for_influencer)),
    path('getCompanyTypes/',csrf_exempt(get_types)),
    path('loginCompany/',csrf_exempt(loginCompany)),
    path('getPopularInfluencers',getPopularInfluencers),
    path('getJobsForCompany/<int:id>',get_jobs_for_company),
    path('updateCompany/',csrf_exempt(updateCompany)),
    path('postJob/',csrf_exempt(postJob)),
    path('uploadImage/job/<int:id>',csrf_exempt(postJobImage)),
    path('uploadImage/influencer/<int:id>',csrf_exempt(postInfluencerImage)),
    path('uploadImage/company/<int:id>',csrf_exempt(postCompanyLogo)),
    path('signUpCompany/',csrf_exempt(signUpCompany)),
    path('updateJob/',csrf_exempt(updateJob)),
    path('deleteJob/<int:id>',csrf_exempt(deleteJob)),
    path('getInfluencersForActiveJob/<int:id>',csrf_exempt(get_influencers_for_active_job)),
    path('finishJob/',csrf_exempt(finish_job)),
    path('chats/<type>/<int:id>',get_all_chats),
    path('messages/<int:id>',get_messages_for_chat),
    path('postMessage/',csrf_exempt(post_message))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
