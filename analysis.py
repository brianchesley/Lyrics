#rock_analysis
#Brian Chesley
import urllib

from collections import Counter
import pickle
import itertools
import pandas as pd
import re
import numpy
import scipy
from ggplot import *
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from random import shuffle

def remove_symbols(dict_file):
    """Cleaning up the files """
    artist = dict_file.keys()[0]
    combined_songs = list(itertools.chain(*dict_file.values()))
    combined_songs = [item for sublist in combined_songs for item in sublist]
    combined_songs = [word.lower() for word in combined_songs]
    combined_songs = [word.replace('\xe2\x80\x99', "'") for word in combined_songs]
    d = {artist : combined_songs}
    pickle.dump(d, open(artist + '_lyrics.pickle', 'wb'))

file = pickle.load(open('rush' + '_lyrics.pickle', 'rb'))

def dog():
    pass

def analysis(dict_file):
    words = dict_file.values()[0]
    shuffle(words)
    word_count = Counter(words[0:17000])
    top_20 = []
    for word in sorted(word_count, key=word_count.get, reverse=True)[:40]:
        if word not in ['the', "i'm", 'to', 'my', 'me', 'you', 'i',\
            'a', 'it', 'your', 'you', 'and', 'on', 'of', 'in', 'is', 'for', 'with',\
            "that", "it's"]:
            top_20.append((word, word_count[word]))
    return (len(words), len(word_count), top_20)

artist_list = ['kiss','metallica','u2', 'aerosmith', 'acdc', 'eagles',\
'rollingstones','bonjovi', 'pinkfloyd', 'ledzeppelin']


#print analysis(file)

def unique_words_dict(artists_list):
    """creates a unique words dict"""
    UWD = {}
    for artist in artists_list:
        file = pickle.load(open(artist + '_lyrics.pickle', 'rb'))
        total_words, unique_words, top_20 = analysis(file)
        UWD[artist] = int(unique_words)
    return UWD
    
def avg_words_song(band):
    """returns the average word count of all songs"""
    count = {}
    file = pickle.load(open(band + '_count.pickle', 'rb'))
    for artist, value in file.iteritems():
        count[artist] = sum(value)/float(len(value))
    return count

print avg_words_song('rush')


def unique_words_df(file):
    """returns a list of tuples with total words v unique words after each word"""
    new = []
    count = 0
    data_points = []
    for artist, words in file.iteritems():
        for word in words:
            count +=1
            if word not in new:
                new.append(word)
            data_points.append((count, len(new)))
    return data_points

def plot_words_v_unique_words():  
    data = dimin_returns(pickle.load(open('metallica_lyrics.pickle', 'rb')))
    headers = ('Count', 'Unique_Words')
    df = pd.DataFrame(data, columns=headers)
    prot = ggplot(df, aes(x='Count', y='Unique_Words')) + geom_point() + geom_line() + ggtitle('Metallica')
    print prot


def all_artists_plot():
    UWD = unique_words_dict(artist_list)
    df = pd.DataFrame(list(UWD.iteritems()), columns=['Artist','Unique_Words'])
    df['Avg_Words_Song'] = count.values()
    print df
    plot = ggplot(df, aes(x='Unique_Words', y='Avg_Words_Song',\
    label="Artist")) + geom_point(color='steelblue', size=100\
    ) + geom_text(angle=45, vjust=-.01) + ggtitle("Rock Vocabulary")
    return plot
