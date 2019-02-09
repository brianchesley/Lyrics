from createDatabase import Database
from lyrics_data_scrape import Artist, Song, Album


database = Database()
database.create_song_table()

drake = Artist('drake')
albums = drake.get_album_infos()

for album in albums:
    album = Album('drake', album)
    print(album.title)
    if album.title in ['Room For Improvement','Comeback Season','So Far Gone','Thank Me Later','Young Sweet Jones',
                       'Take Care', 'Scorpion','More Life','Views','What A Time To Be Alive',
                       "If You're Reading This It's Too Late",'Nothing Was The Same','Scary Hours']:
        pass
    else:
        for song in album.songs:
            song_class = Song(album.artist_name, song)
            row = (song_class.song_name, song_class.artist_name, album.type, album.title, album.year, song_class.lyrics)
            database.insert(row)

