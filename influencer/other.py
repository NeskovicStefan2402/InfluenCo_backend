import urllib.request
import requests
# from influenCo.settings import MEDIA_ROOT
import json
from bs4 import BeautifulSoup
def youtubeSubscribers(name):
    key = "AIzaSyA8e2wuvlNnZpFubhTVuxfEL2KLzZYu4Wc"
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    return int(subs)

def facebookImage(url,email):
    soup = BeautifulSoup(urllib.request.urlopen(url))
    image_path=MEDIA_ROOT+'/'+str(email).replace('.','')+'.jpg'
    default_image_url='https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png'
    try:
        urllib.request.urlretrieve(soup.find('img',{'class':'_11kf img'})['src'],image_path)
    except Exception as e:
        print(e)
        urllib.request.urlretrieve(default_image_url,MEDIA_ROOT+'/'+image_path)

def facebookLikes(url):
    # token='EAALPTeaV6x0BAE2QZBBOoGbNyQJwnDmZB9CnPb1XWegNqwAfajT4eDYtc8gHwZCmhLsMC24Ra873wEu6uiQv1cqleWi9kgXMpyMZCisbfrrC8zpVDrLquQm7JOqI1bOJ6cXEYB0o2LycGrdH2EcVszyhC7bPMQaGz5RAr6QhjlMZCL84hvSOCEBRDyuZAwTefHelPob2tzTqZBU3xv9jhaep80hHZA2a6veZASGfKJAJr6AZDZD'
    # url='https://graph.facebook.com/'+user+'?fields=birthday,email,hometown&access_token=790883441437469 '
    # jsonString=requests.get(url).content.decode('utf-8')
    # jsonObject=json.loads(jsonString)
    # print(jsonObject)
    soup = BeautifulSoup(urllib.request.urlopen(url))
    print(soup.find('span',{'class':'_3d0'}))
    # # lista_a=soup.find('span',{'class':'_50f8 _2iem'}).find_all('a')
    # for i in lista_a:
    #     print(i.text)

facebookLikes('https://www.facebook.com/stefan.neskovic.10/friends')