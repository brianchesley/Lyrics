import unittest
from lyrics_data_scrape import Artist



class LyricsTest(unittest.TestCase):
    def test_song_list(self):
        artist = Artist('drake')
        songs = artist.get_song_list()
        print(songs)
        self.assertIs(type(songs), type([]))



if __name__ == '__main__':
    unittest.main()

