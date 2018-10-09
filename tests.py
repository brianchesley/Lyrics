import unittest
from lyrics_data_scrape import Artist, Song



# class ArtistTest(unittest.TestCase):
#     def test_song_list(self):
#         artist = Artist('drake')
#         songs = artist.get_song_list()
#         print(songs)
#         self.assertIs(type(songs), type([]))

class SongTest(unittest.TestCase):
    def test_lyrics(self):
        song = Song('drake','Where Were You')
        print(song.get_lyrics())

if __name__ == '__main__':
    unittest.main()

