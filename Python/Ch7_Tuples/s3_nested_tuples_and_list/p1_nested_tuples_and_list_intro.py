albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))  # 5

# 1st way to access nested tuples (using indexes).
for album in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album[0], album[1], album[2]))

print()

# 2nd way to access nested tuples (using unpacking the tuple).
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print()

# 3rd way to access nested tuples (most efficient).
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))


