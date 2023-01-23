shopping_list = ["pasta", "eggs", "milk", "chocolate", "bread", "rice"]

user_input = input("Enter the name of the item that you want to search: ")

position = None

for each_item in shopping_list:
    if each_item == user_input:
        position = shopping_list.index(each_item)
        break


if position is not None:
    print(f"Index of {user_input} is: {position}")
else:
    print(f"{user_input} is not present in shopping_list")