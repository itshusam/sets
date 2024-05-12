artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()


for artist in artist_names:
    unique_artists.add(artist)


duplicate_playlists_found = len(unique_artists) != len(artist_names)


print("Duplicate playlists found:", duplicate_playlists_found)