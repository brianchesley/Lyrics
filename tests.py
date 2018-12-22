import unittest
from lyrics_data_scrape import Artist, Song



class ArtistTest(unittest.TestCase):
    def test_song_list(self):
        artist = Artist('drake')
        songs = artist.get_song_list()
        self.assertIs(type(songs), type([]))

class SongTest(unittest.TestCase):
    def test_lyrics(self):
        song = Song('drake','Where Were You')
        lyrics = song.get_lyrics()
        self.assertIs(type(lyrics), type([]))
        self.assertIs(song.get_song_url(), 'https://www.azlyrics.com/lyrics/drake/wherewereyou.html')

if __name__ == '__main__':
    unittest.main()

