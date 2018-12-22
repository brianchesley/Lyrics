import sqlite3


class Database():
    def __init__(self):
        self.con = sqlite3.connect('database/lyricsdb.sqlite3')

    def create_song_table(self):
        sql = """
        CREATE TABLE SONGS (
        SONG_NAME TEXT PRIMARY KEY,
        ARTIST TEXT NOT NULL,
        ALBUM_TYPE TEXT,
        ALBUM_NAME TEXT,
        ALBUM_YEAR INTEGER,
        LYRICS TEXT
        )
        """
        self.con.execute(sql)

    def delete_song_table(self):
        sql = '''
        drop table songs'''
        self.con.execute(sql)

    def delete_songs_where(self, song_name):
        sql = "delete from SONGS where SONG_NAME = ?"
        cur = self.con.cursor()
        cur.execute(sql, song_name)


    def insert(self, row):
        try:
            c = self.con.cursor()
            sql = ''' INSERT INTO SONGS (SONG_NAME, ARTIST, ALBUM_TYPE, ALBUM_NAME, ALBUM_YEAR,
                    LYRICS) VALUES (?, ?, ?, ?, ?, ?);
                '''
            c.execute(sql, row)
            self.con.commit()
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(row))
