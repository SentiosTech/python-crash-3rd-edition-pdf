def make_album(artist_name, album_name, album_song_number = None):
    artist_info = {'artist': artist_name, 'album': album_name}
    if album_song_number:
        artist_info['album_song_number'] = album_song_number
    return artist_info

artist = make_album('joe','doe')
print(artist)

artist2 = make_album('gi','joe')
print(artist2)

artist3 = make_album('hitman', 'hart', album_song_number=10)
print(artist3)


