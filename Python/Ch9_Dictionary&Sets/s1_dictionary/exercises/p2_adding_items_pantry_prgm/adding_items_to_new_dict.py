from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:

    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0)+amount


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

# inserting into dict_key using enumerate: makes tuple of values.
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

# Using a dict here as it prevents duplicates
shopping_list = {}

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input("Enter a no for the item : ")

    if choice == "0":
        break

    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"*** You have selected {selected_item} ***")
        print(f"Checking ingredients !!!!!!!!!!!")
        ingredients = recipes[selected_item]
        print(f"Ingredients needed are:  {ingredients}")

    for food_items, required_quantity in ingredients.items():
        quantity_in_pantry = pantry.get(food_items, 0)
        if required_quantity <= quantity_in_pantry:
            print(f"\t {food_items} OK")
        else:
            quantity__to_buy = required_quantity - quantity_in_pantry
            print(f"\t You need to buy {quantity__to_buy} of {food_items}")
            add_shopping_item(shopping_list, food_items, quantity__to_buy)

print(shopping_list)
for things in shopping_list.items():
    print(things)
