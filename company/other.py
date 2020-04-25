import urllib.request
from influenCo.settings import MEDIA_ROOT

def default_image(name):
    default_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRkZqkEFslaphQDNXw1kXJn0kFomsBEnzxy9Vpu2TX9c2Qvcxtn&usqp=CAU'
    image_path=MEDIA_ROOT+'/companies/'+str(name).replace('.','')+'.jpg'
    urllib.request.urlretrieve(default_url,image_path)