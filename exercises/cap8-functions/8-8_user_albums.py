def make_album(artist_name, album_name):
    artist_info = {'artist': artist_name, 'album': album_name}
    return artist_info

while True:
    print("\nPlease enter your artis data")
    print("(enter 'q' at any time to quit)")
    a_name = input("Artist name: ")
    if a_name == 'q':
        print("exit...")
        break
    al_name = input("Album Name: ")
    if al_name == 'q':
        print("exit...")
        break

    artist_data = make_album(a_name, al_name)
    print(artist_data)


