import requests
from bs4 import BeautifulSoup
import re
import os
from hashlib import sha1
import random
from nltk.tokenize import TweetTokenizer

class makeRequest():
    baseURL = 'http://www.azlyrics.com/'
    USER_AGENTS = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36']
    def get(self, url, user_agent=True):
        if user_agent:
            return requests.get(url, headers={'User-Agent': random.choice(self.USER_AGENTS)})
        return requests.get(url)

class Song(makeRequest):
    HTML_TAGS = ['br','div', 'i']
    def __init__(self, artist_name, song_name):
        super().__init__()
        self.song_name = song_name
        self.artist_name = artist_name

    def get_lyrics(self):
        soup = BeautifulSoup(self.get_song_page(), 'lxml')
        page_lyric = soup.find_all("div", limit=22)[-1] # lyrics start on 22nd div
        lyrics = ''.join(page_lyric.find_all(text=True))
        tknzr = TweetTokenizer()
        lyrics = tknzr.tokenize(lyrics)
        lyrics = [word for word in lyrics if word not in self.HTML_TAGS]
        return lyrics[20:]

    def get_song_url(self):
        print('song name',self.song_name)
        song_url = re.sub(r'[^\w\s]','', self.song_name).replace(" ",'').lower()
        base = 'http://www.azlyrics.com/lyrics/'
        rest = self.artist_name + '/' + song_url + '.html'
        return base + rest

    def get_song_page(self):
        url = self.get_song_url()
        response = makeRequest.get(self, url)
        return response.content

class Artist(makeRequest, Album):
    def __init__(self, artist_name):
        super().__init__()
        self.artist_name = artist_name

    def get_song_list_page(self):
        url = self.baseURL + self.artist_name[0] + '/' + self.artist_name + '.html'
        response = makeRequest.get(self, url)
        return response

    def get_song_list(self):
        soup = BeautifulSoup(self.get_song_list_page().content, 'lxml')
        songs = []
        for song in soup.findAll(target='_blank'):
            songs.append(str(song.text))
        return songs

    def get_album_information(self):
        soup = BeautifulSoup(self.get_song_list_page().content, 'lxml')
        album_infos = []
        for album in soup.findAll("div", {"class": "album"}):
            album_infos.append(album.text)
        return album_infos

class Album():
    def __init__(self, , album_info):
        super().__init__()
        self.album_info = album_info
        self.album_title =
        self.album_type =
        self.year =

    def parse_album_info(self):
        album_info_split = self.album_info.split(':', 1)
        self.album_title = album_info_split[0]
        album_title_year = album_info_split




