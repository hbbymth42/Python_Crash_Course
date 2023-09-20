def make_album(title, artist, num_songs=None):
    album = {'title': title.title(), 'artist': artist.title()}
    if num_songs:
        album['num_songs'] = int(num_songs)
    return album

while True:
    print("\nPlease tell us your favourite album")
    print("(Enter 'q' at any time to quit)")

    album_title = input("Album Title: ")
    if album_title == 'q':
        break

    artist_name = input("Artist Name: ")
    if artist_name == 'q':
        break

    n_songs = input("Number of Songs (Optional; Press Enter to Skip): ")
    if n_songs == 'q':
        break

    favourite_album = make_album(title=album_title, artist=artist_name,
                                 num_songs=n_songs)
    print(favourite_album)