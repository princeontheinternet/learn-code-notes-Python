#                   Section 8: Break Statement

# Break statement terminates the loop or jumps out of the loop. It can be useful if you are searching through a list
#   containing 1000 items and if u find the item before reaching 1000 then there's no point in looking for rest of the
#   items

shopping_list = ["pasta", "eggs", "milk", "chocolate", "bread", "rice"]
print(shopping_list)

item_to_be_found = input("Please Enter the name of the item that you want to find: ")
found_at = None                     # None keyword is used to define a null value, or no value at all.

for i in range(len(shopping_list)):
    if shopping_list[i] == item_to_be_found:
        found_at = i
        break                                   # As soon as the item is found this will break the entire loop

if found_at is not None:
    print("Item {} found at position {}".format(item_to_be_found, found_at))
else:
    print("Item {} not found".format(item_to_be_found))


#   Output:

# Please Enter the name of the item that you want to find: milk
# Item milk found at position 2
