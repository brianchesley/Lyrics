import sqlite3


class Database():
    def __init__(self):
        con = sqlite3.connect('/database/db.sqlite3')

    def create_song_table(self):
        sql = """
        CREATE TABLE SONGS (
        SONG TEXT PRIMARY KEY,
        ARTIST TEXT NOT NULL,
        
        """