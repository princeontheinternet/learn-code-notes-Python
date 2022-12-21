# List:

"""

    1. Lists is a Sequence Data Type.
    2. Lists are ordered (the way things are inserted/stored) and Indexed.
    3. Lists are Mutable.
        1. Therefore, Lists are Addable and Changeable(as they are Indexed & Mutable).
    4. Lists Allows Duplicates (as they are Indexed).

"""

computer_parts = ["keyboard", "mouse", "cpu", "monitor", "printers", "speakers"]

for i in computer_parts:
    print(i)

# You can also slice a list.
print(computer_parts[0:3])  # slicing a list in a range will give you another list.
print(computer_parts[-1])


#   Output:

# keyboard
# mouse
# cpu
# monitor
# printers
# speakers
# ['keyboard', 'mouse', 'cpu']
# speakers
