def city_country(city,country):
    print('"' + city + ', ' + country + '"')
city_country('Mumbai','India')
city_country('Bangalore','India')
city_country('Chennai','India')
def make_album(artist,title,tracks=''):
    """ Display a simple dictionary representing album """
    album_dict = {
        'artist':artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

while True:
    artist = input('Who is your favourite artist ?')
    if artist == 'q':
        break
    title = input('Which album of him do you like ? ')
    if title == 'q':
        break
    
    album = make_album(artist, title)
    print(album)

