import urllib.request
import requests
from influenCo.settings import MEDIA_ROOT
import json
from bs4 import BeautifulSoup
def youtubeSubscribers(name):
    key = "AIzaSyA8e2wuvlNnZpFubhTVuxfEL2KLzZYu4Wc"
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCG8rbF3g2AMX70yOd8vqIZg&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    return int(subs)

def instagramFollowers(name):
    data = urllib.request.urlopen('https://www.instagram.com/'+name+'/?__a=1').read()
    followers = json.loads(data)["graphql"]['user']["edge_followed_by"]["count"]
    return int(followers)


def facebookImage(url,email):
    default_image_url='https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png'
    image_path=MEDIA_ROOT+'/'+str(email).replace('.','')+'.jpg'
        
    try:
        soup = BeautifulSoup(urllib.request.urlopen(url))
        urllib.request.urlretrieve(soup.find('img',{'class':'_11kf img'})['src'],image_path)
        print('Ucitao sliku')
    except Exception as e:
        print(e)
        urllib.request.urlretrieve(default_image_url,image_path)

# facebookImage('https://www.facebook.com/matejaa.neskovic','matejaneskovic005@gmail.com')
