import requests
from bs4 import BeautifulSoup
import re
import string
from time import sleep
import random
import pickle
import urllib
from urllib2 import urlopen
import os
from hashlib import sha1    
    
    
def check_proxy(proxies):      
    for i in proxies:
        try:
            urllib.urlopen('http://www.azlyrics.com/', proxies=i)
        except:
            print "This proxy doesn't work ", i
        else:
            print 'All good! here! ', i

def check_proxy(proxies):      
    for i in proxies:
        try:
            response = requests.get('http://www.azlyrics.com/', proxies=i)
        except:
            print "This proxy doesn't work ", i
        else:
            print 'All good! here! ', i
            print response.content
            


def get_songs(proxies, user_agents, artists):
    """takes a list of dictionaries for request"""
    base = 'http://www.azlyrics.com/'
    art_song_dict = {}
    for artist in artists:    
        url = base + artist[0] + '/' + artist + '.html'
        sleep(random.randint(0,10))
        response = requests.get(url, headers = {'User-Agent': random.choice(user_agents)}, proxies=random.choice(proxies))
        soup = BeautifulSoup(response.content, 'lxml')
        lang = []
        for song in soup.findAll(target='_blank'):
            lang.append(str(song.text))
        art_song_dict[artist] = lang
        pickle.dump(art_song_dict, open(artist + '_songs.pickle', 'wb'))
    return art_song_dict



def get_url_AZ(artist, song):
       
    song = re.sub('['+string.punctuation+']', '', song).replace(' ','').lower()
    base = 'http://www.azlyrics.com/lyrics/'
    rest = artist + '/' + song + '.html'
    return base + rest


def get_lyric_AZ(url, proxies, user_agents):

    if load_local(url):
        soup = BeautifulSoup(load_local(url), 'lxml')
        page_lyric = soup.findAll(style="margin-left:10px;margin-right:10px;")
        lyric = re.sub('[(<.!,;?>/\-)]', " ",  str(page_lyric)).split()
        lyric = [word for word in lyric if word != 'br']
        return lyric[10:-4]
    else:
        sleep(random.randint(0,20))
        response = requests.get(url, headers = {'User-Agent': random.choice(user_agents)}, proxies = random.choice(proxies))
        store_local(url, response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        page_lyric = soup.findAll(style="margin-left:10px;margin-right:10px;")
        lyric = re.sub('[(<.!,;?>/\-)]', " ",  str(page_lyric)).split()
        lyric = [word for word in lyric if word != 'br']
        return lyric[10:-4]


CACHE_DIR = os.path.join(os.path.dirname(__file__), 'cache')

def url_to_filename(url):
    #Make a URL into a file name, using SHA1 hashes. 

    # use a sha1 hash to convert the url into a unique filename
    hash_file = sha1(url).hexdigest() + '.html'
    return os.path.join(CACHE_DIR, hash_file)


def store_local(url, content):
     #Save a local copy of the file.

    # If the cache directory does not exist, make one.
    if not os.path.isdir(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    # Save to disk.
    local_path = url_to_filename(url)
    with open(local_path, 'wb') as f:
        f.write(content)


def load_local(url):
       # Read a local copy of a URL.
    local_path = url_to_filename(url)
    if not os.path.exists(local_path):
        return None

    with open(local_path, 'rb') as f:
        return f.read()


def main():
    master_dict = {}
    avg_dict = {}
    with open('rush_songs.pickle', 'rb') as f:
        art_info = pickle.load(f) 
    for artist, songs in art_info.iteritems():
        avg = []
        lyrics = []
        for song in songs:
            print artist, song
            url = get_url_AZ(artist,song)
            lyric = get_lyric_AZ(url, proxies, user_agents)
            print lyric
            avg.append(len(lyric))
            lyrics.append(lyric)
        avg_dict[artist] = avg
        master_dict[artist] = lyrics
        print artist, "-------------------------completed----------------------------------"
        pickle.dump(avg_dict, open(artist + '_count.pickle', 'wb'))
        pickle.dump(master_dict, open(artist + '_lyrics.pickle', 'wb'))
    return 'Fully Completed!'

user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19']
proxies = [{"http": "http://107.170.13.140:3128"}, {"http": "http://198.23.67.90:3128"}]

#check_proxy(proxies)
main()