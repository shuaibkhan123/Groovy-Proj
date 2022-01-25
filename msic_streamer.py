import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup


def search_reults(song_name):
    music_name =song_name
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    titles=[]
    urls=[]

   
    for i in range(0,6):
        audio=requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[i]))
        url="https://www.youtube.com/watch?v=" + "{}".format(search_results[i])

        inspect = BeautifulSoup(audio.content, "html.parser")
        yt_title = inspect.find_all("meta", property="og:title")
        for concatMusic1 in yt_title:
            pass
        titles.append(concatMusic1['content'])
        urls.append(url)
        #print(concatMusic1['content'])
        #rint(url)
    

def play_song(song_name):
    music_name =song_name
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    audio=requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    url="https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    inspect = BeautifulSoup(audio.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")
    for concatMusic1 in yt_title:
        pass
    result=[]
    result.append(concatMusic1['content'])
    result.append(url)
    return result

