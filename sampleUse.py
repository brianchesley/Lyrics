from createDatabase import Database
from lyrics_data_scrape import Artist, Song, Album


database = Database()
# database.delete_song_table()
# database.create_song_table()
# database.insert(('views','drake','rap','views',2009, 'BLAHBLAHBALH'))
# database.delete_songs_where(('views',))

drake = Artist('drake')
albums = drake.get_album_info()



views = Album(albums[10])

for song in views.songs:
    song_class = Song(views.artist_name, song)
    row = (song_class.song_name, song_class.artist_name, views.type, views.title, views.year, song_class.lyrics)
    database.insert(row)

