# Tuples:

"""

    1. Tuples are Sequence Data Type.
    2. Tuples are ordered (the way things are inserted/stored) and indexed.
    3. Tuples are Immutable.
        1. Therefore, Tuples are not Addable and UnChangeable.
    4. Tuples allows Duplicates (as they are Indexed).


Advantages of Tuples

    1. Protects the Data Integrity (as they are Immutable)

    2. Unpacking a tuple is flawless.

    3. Tuples use less memory compares to lists.

"""

eg_of_tuples = "a", "b", "c"
print(eg_of_tuples)  # ('a', 'b', 'c')

metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)  # ('Ride the Lightning', 'Metallica', 1984)
print(metallica[0])  # Ride the Lightning
print(metallica[1])  # Metallica
print(metallica[2])  # 1984

a = 1,
print(type(a))   # <class 'tuple'>

# *** 1st advantage of tuples ***

# TUPLES ARE IMMUTABLE:

# Since tuples are immutable you cannot change their values and
# therefore it protects the integrity of your data for eg:
# metallica[0] = "Master of Puppets"  # this line shows error
# but if u convert this to list and change the value it is possible eg:

new_list = list(metallica)
print(new_list)  # ['Ride the Lightning', 'Metallica', 1984]
new_list[0] = "Master of Puppets"
print(new_list)  # ['Master of Puppets', 'Metallica', 1984]

# *** 2nd Advantage of tuples ***

# UNPACKING OF A TUPLE:

print("Unpacking a list")
data_list = [12, 13, 14]
data_list.append(15)  # When you append 15 then u get error in the next line
p, q, r = data_list
print(p)
print(q)
print(r)

print("Unpacking a tuple")
data_tuple = 1, 2, 76  # data represents a tuple
x, y, z = data_tuple
print(x)
print(y)
print(z)
# You wont get error here as we can't append a value to a tuple as they are immutable.
# Therefore, you can always unpack them successfully.

# Advantages of Tuples:

# 1. Tuples use less memory compares to lists
# 2. Protect against unintended changes to your data as they are immutable.
# 3. Helps prevent bugs as they can be unpacked easily
# because they always contain the expected no of items
# and items cannot be added or removed as they are immutable.


# When to use Tuples?

# 1. Tuples are heterogeneous where as list are more efficient with homogenous items.

# 2. If you do not want to add or remove items,
# you can use tuples as tuples are immutable so you cannot add or remove items from it
# whereas lists are mutable and you can add or remove items from it.

# 3. When u want to unpack you can use tuples.
