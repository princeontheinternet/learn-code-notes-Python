# Importance of Unpacking.

metallica = "Ride the Lightning", "Metallica", 1984  # this is a tuple.

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

title, artist, year = metallica
print(title)    # Ride the Lightning
print(artist)   # Metallica
print(year)     # 1984

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])  # 20000
# this is not a efficient way as
#   we may forget or get confused with the indexes.
# It is advices to unpack the tuple and use variables instead.

# Unpacking the tuple into variable.
name, length, width, height, price = table
# using variable names
print(length * width)   # 20000


