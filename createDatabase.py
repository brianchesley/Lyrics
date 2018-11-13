import sqlite3


class Database():
    def __init__(self):
        self.con = sqlite3.connect('database/lyricsdb.sqlite3')

    def create_song_table(self):
        sql = """
        CREATE TABLE SONGS (
        SONG TEXT PRIMARY KEY,
        ARTIST TEXT NOT NULL,
        ALBUM_TYPE TEXT,
        ALBUM_NAME TEXT,
        ALBUM_YEAR INTEGER
        )
        """
        self.con.execute(sql)


    def insert(self):
        try:
            c.execute("INSERT INTO SONGS VALUES (123456, 'test')". \
            format(tn='SONGS', idf=id_column, cn=column_name))
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
