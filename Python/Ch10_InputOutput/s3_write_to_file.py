# Write to a file

# cities = ['Mumbai', 'Pune', 'Delhi', 'Nagpur']
#
# with open('cities.txt', 'w') as city_file:
#     for i in cities:
#         print(i, file=city_file)

cities_in_Python = []

with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities_in_Python.append(city.strip("\n"))  # it strips \n as strips removes stuffs from beginning and from end

print(cities_in_Python)

