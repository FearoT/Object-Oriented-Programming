class Song:
    c = 6

    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number
        artist.add_song(self)

    """def display(self, a, b):
        c = 19
        a = self.c + 5
        b = c + 5
        return a, b

    def display2(self, d, e):
        e = d - self.c
    """


#  metin olarak algılıyo üç tane çift tırnak
#  s = Song("a", "b", "c", 1)
#  print(s.display(10, 10))


class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []
        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist
        track_number = len(self.tracks)
        song = Song(title, artist, self, track_number)
        self.tracks.append(song)


#  album1 = Album("ad", "aa", 14)
#  b = Song("a", "b", album1, 1)

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


band = Artist("Bob's Awsome Band")
album = Album("Bob's Fist Single", band, 2013)
album.add_track("A Ballad about Cheese")
album.add_track("A Ballad abaout Cheese (dance remix)")
album.add_track("A Third Song to Use Up the Rest of the Space")

playlist = Playlist("My Favourite Songs")
playlist.add_song(album.tracks[2])
