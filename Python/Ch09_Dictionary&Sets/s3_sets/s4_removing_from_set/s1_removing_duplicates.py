
data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates.

# unique_data = set(data)
unique_data = sorted(set(data))     # sorted data but will give list as o/p
print(unique_data)


# Create a list of unique colours, keeping the order they appeared.
unique_data = list(dict.fromkeys(data))
print(unique_data)

