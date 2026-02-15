# 8.6 city names
def city_country(city, country):
    formatted_message = f"{city.title()}, {country.title()}"
    return formatted_message


# function calls
print(city_country("fiorano", "italy"))
print(city_country('paris', 'italy'))
print(city_country('buenos aires', 'argentina'))

# 8.7 music album


def make_album(band, album, tracks_number=''):
    record = {}
    if tracks_number:
        record['band_name'] = band
        record['album_name'] = album
        record['number of tracks'] = tracks_number
    else:
        record['band_name'] = band
        record['album_name'] = album

    return record


# function calls for 3 albums
print(make_album("nirvana", 'nevermind', 12))
print(make_album("oasis", "definitely maybe"))
print(make_album("oasis", "don't believe the truth"))

# 8.8 user albums in a while loop
flag = True
albums = []
while flag:
    print(f"type quit when you're done")
    band = input("Type the name of the band : ")
    album = input("Type the name of the album : ")
    albumm_info = make_album(band, album)
    albums.append(albumm_info)
    more_data = input("continue ? ")
    if more_data == "quit":
        flag = False
for album in albums:
    for key, value in album.items():
        print(f"{key} : {value}")
