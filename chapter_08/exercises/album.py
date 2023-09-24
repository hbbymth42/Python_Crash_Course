def make_album(title, artist, num_songs=None):
    album = {'title': title.title(), 'artist': artist.title()}
    if num_songs:
        album['num_songs'] = num_songs
    return album

favourite_album_1 = make_album(title='the velvet rope', artist='janet jackson')
favourite_album_2 = make_album(title='illmatic', artist='nas', num_songs=10)

print(favourite_album_1)
print(favourite_album_2)