import requests
from bs4 import BeautifulSoup
import re
import string
from time import sleep
import random
import pickle
import os
from hashlib import sha1

class AzBase():
    def __init__(self):
        self.baseUrl = 'http://www.azlyrics.com/lyrics/'
    def get_base_url(self):
        return self.baseUrl

class Artist(AzBase):
    def __init___(self, artist_name):
        super()
        AzBase()
        self.artist_name = artist_name

    def get_song_list(self):
        url = AzBase.get_base_url() + self.artist_name[0] + '/' + self.artist_name + '.html'
        sleep(random.randint(0, 10))
        response = requests.get(url, headers={'User-Agent': random.choice(USER_AGENTS)}, proxies=random.choice(PROXIES))
        soup = BeautifulSoup(response.content, 'lxml')
        songs = []
        for song in soup.findAll(target='_blank'):
            songs.append(str(song.text))
        return songs

class Song(AzBase):
    def __init__(self, songName, artistName):
        super()
        AzBase()
        self.lyrics = None
        self.url = None
        self.song_name = songName
        self.artist_name = artistName
        self.song_page = self.get_song_page()

    def get_lyrics(self):
        soup = BeautifulSoup(self.song_page, 'lxml')
        page_lyric = soup.findAll(style="margin-left:10px;margin-right:10px;")
        lyric = re.sub('[(<.!,;?>/\-)]', " ",  str(page_lyric)).split()
        lyric = [word for word in lyric if word != 'br']
        return lyric[10:-4]

    def get_song_url(self):
        song_url = re.sub('['+string.punctuation+']', '', self.song).replace(' ','').lower()
        base = 'http://www.azlyrics.com/lyrics/'
        rest = self.artist + '/' + song_url + '.html'
        return base + rest

    def get_song_page(self):
        response = requests.get(self.get_song_url(), headers={'User-Agent': random.choice(user_agents)}, proxies = random.choice(proxies))
        return response

class Cache():

    def __init__(self):
        self.CACHE_DIR = os.path.join(os.path.dirname(__file__), 'cache')

    def url_to_filename(self, url):
        # Make a URL into a file name, using SHA1 hashes.
        # use a sha1 hash to convert the url into a unique filename
        hash_file = sha1(url).hexdigest() + '.html'
        return os.path.join(self.CACHE_DIR, hash_file)


    def store_local(self, url, content):
        #Save a local copy of the file.
        # If the cache directory does not exist, make one.
        if not os.path.isdir(self.CACHE_DIR):
            os.makedirs(self.CACHE_DIR)

        # Save to disk.
        local_path = self.url_to_filename(url)
        with open(local_path, 'wb') as f:
            f.write(content)

    def load_local(self, url):
        # Read a local copy of a URL.
        local_path = self.url_to_filename(url)
        if not os.path.exists(local_path):
            return None

        with open(local_path, 'rb') as f:
            return f.read()


USER_AGENTS = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19']
PROXIES = [{"http": "http://107.170.13.140:3128"}, {"http": "http://198.23.67.90:3128"}]
