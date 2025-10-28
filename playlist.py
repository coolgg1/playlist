liked_songs = {
    "Shake It Off": {"artist": "Taylor Swift", "duration": (3, 23), "genre": "Pop"},
    "Shemesh": {"artist": "Mergi", "duration": (2, 33), "genre": "Israeli"},
    "Chop Suey!": {"artist": "System of a Down", "duration": (3, 30), "genre": "Metal"},
    "Mimaamakim": {"artist": "Idan Raichel", "duration": (4, 33), "genre": "Israeli"},
    "Do I Wanna Know?": {"artist": "Arctic Monkeys", "duration": (4, 26), "genre": "Rock"},
    "Love Story": {"artist": "Taylor Swift", "duration": (3, 55), "genre": "Pop"},
    "Bo’ee": {"artist": "Idan Raichel", "duration": (4, 45), "genre": "Israeli"}
}


def print_playlist(playlist):
    print("\n🎶 Updated Playlist:")
    for song, info in playlist.items():
        minutes, seconds = info['duration']
        print(f"- {song} by {info['artist']} ({minutes}:{seconds:02d}) - {info['genre']}")


def main():
    liked_songs["Smells Like Teen Spirit"] = {
        "artist": "Nirvana", "duration": (5, 1), "genre": "Rock"
    }
    liked_songs["Blinding Lights"] = {
        "artist": "The Weeknd", "duration": (3, 20), "genre": "Pop"
    }
    liked_songs["Hotel California"] = {
        "artist": "Eagles", "duration": (6, 30), "genre": "Rock"
    }

    print("Playlist after adding new songs:")
    print_playlist(liked_songs)

    song_name = input("\nEnter a song name to check if it exists: ")

    if song_name in liked_songs:
        remove = input(f"'{song_name}' found! Do you want to remove it? (yes/no): ").lower()
        if remove == "yes":
            del liked_songs[song_name]
            print(f"'{song_name}' has been removed.")
    else:
        print(f"'{song_name}' is not in the playlist.")

    artist_name = input("\nEnter an artist you don't like to remove all their songs: ")


    removed_songs = [song for song, info in liked_songs.items()
                     if info["artist"].lower() == artist_name.lower()]

    for song in removed_songs:
        del liked_songs[song]

    if removed_songs:
        print(f"Removed all songs by {artist_name}: {removed_songs}")
    else:
        print(f"No songs by {artist_name} were found.")
    print_playlist(liked_songs)

if __name__ == "__main__":
    main()