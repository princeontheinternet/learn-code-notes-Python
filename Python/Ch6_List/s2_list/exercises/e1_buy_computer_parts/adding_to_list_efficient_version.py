available_parts = ["mouse", "keyboard", "printer", "CPU", "dvd_drive", "hdmi_cable"]
computer_parts = []

valid_choice = []
for i in range(1, len(available_parts) + 1):
    valid_choice.append(str(i))
# print(valid_choice)  # TODO: Remove after testing

choice = "-"
while choice != "0":
    if choice in valid_choice:
        index = int(choice) - 1
        chosen_part = available_parts[index]
        print("Adding {}".format(chosen_part))
        computer_parts.append(chosen_part)
        print("Do u want to add anything else? Press 0 to exit")
    else:
        print("What do u want to buy? The options are:")
        for number, value in enumerate(available_parts):
            print("{}: {}".format(number + 1, value))
        print("Type the number for the item you want to buy: ")
    choice = input()

print("You have bought: {}".format(computer_parts))
