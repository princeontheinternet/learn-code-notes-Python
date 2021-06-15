# List:

"""
    1. A list is a collection which is ordered and changeable.
    2. Allows duplicate members.
    3. List are Mutable objects.
    4. List is a sequence data type.
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
