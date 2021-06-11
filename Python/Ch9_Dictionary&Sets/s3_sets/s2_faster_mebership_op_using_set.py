# Referring to Ch6_List/s2_list/exercises/e1_buy_computer_parts/adding_to_list_basic_version.py


choice = "-"  # initialise choice to something invalid
while choice != "0":
    # if choice in "12345":     # 123 gives o/p ->  you chose  123
    # if choice in list("12345"):   # the above bug fixed
    # if choice in set("12345"):
    if choice in {'1', '2', '3', '4', '5'}: # Fastest Performance
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
