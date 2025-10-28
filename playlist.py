liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}


def AddSongsToPlaylist():
    new_songs = {
        "Blinding Lights": {
            "artist": "The Weeknd",
            "duration": (3, 20),
            "genre": "Pop"
        },
        "Smells Like Teen Spirit": {
            "artist": "Nirvana",
            "duration": (5, 1),
            "genre": "Rock"
        },
        "Imagine": {
            "artist": "John Lennon",
            "duration": (3, 3),
            "genre": "Rock"
        }
    }
    liked_songs.update(new_songs)
    print(liked_songs)


def RemoveSongFromPlaylist():
    song_to_remove = "Shake It Off"
    if song_to_remove in liked_songs:
        liked_songs.pop(song_to_remove)
    print(liked_songs)

def PrintPlaylist():
    artist_to_remove = "Taylor Swift"
    songs_to_remove = [song for song, details in liked_songs.items() if details["artist"] == artist_to_remove]
    for song in songs_to_remove:
        liked_songs.pop(song)
    print(liked_songs)

def main():
    AddSongsToPlaylist()
    RemoveSongFromPlaylist()
    PrintPlaylist()


main()
