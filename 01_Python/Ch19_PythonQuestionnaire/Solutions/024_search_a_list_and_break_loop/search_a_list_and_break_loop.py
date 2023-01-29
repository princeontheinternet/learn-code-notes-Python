shopping_list = ["pasta", "eggs", "milk", "chocolate", "bread", "rice"]

user_input = input("Enter the name of the item that you want to search: ")

# Method 1: Without index method
position = None

for i in range(0, len(shopping_list)-1):
    if shopping_list[i] == user_input:
        position = i
        break


if position is not None:
    print(f"Index of {user_input} is: {position}")
else:
    print(f"{user_input} is not present in shopping_list")


# Method 2: Using Index method

try:
    found_at = shopping_list.index(user_input)
    print(f"Index of {user_input} is: {found_at}")
except ValueError:
    print(f"{user_input} is not present in shopping_list")
except:
    print("Something went wrong")

shopping_list.index(user_input)
