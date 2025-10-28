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
    """
    You see Maya's playlist songs liked and are not so happy with it, so you want to add your own songs
    to the playlist of favorite songs.
    Add at least 3 songs you like to the playlist and finally print the updated playlist.

    What will happen if you find out that there is something there? Kiki Barberashi Hashashm
    """
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
    """
    Maya wants to check if you have included specific songs (by song name). Write a code that allows her to check if a particular song exists,
    If it exists and she doesn't want it, she will remove it.

    What will happen if Mom accidentally taps on the keyboard "Oh, there's a pop-up."
    and dont use "del"
    """
    song_to_remove = "Shake It Off"
    if song_to_remove in liked_songs:
        liked_songs.pop(song_to_remove)
    print(liked_songs)

def PrintPlaylist():
    """
    In the next step, Maya looks at the songs you added but she doesn't like some of the artists you added and therefore wants to remove
    all the songs by that artist from the playlist songs liked.
    
    What would happen if Mama would play a song by Mama Three Kiki Barbershi hahaha
    """
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