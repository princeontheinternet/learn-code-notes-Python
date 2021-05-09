available_parts = ["mouse", "keyboard", "printer", "CPU", "dvd_drive", "hdmi_cable"]
computer_parts = []

choice = "-"
while choice != "0":
    if choice in "123456":
        print("Adding {} to the list.".format(choice))

        if choice == "1":
            computer_parts.append("mouse")
        elif choice == "2":
            computer_parts.append("keyboard")
        elif choice == "3":
            computer_parts.append("printer")
        elif choice == "4":
            computer_parts.append("CPU")
        elif choice == "5":
            computer_parts.append("dvd_drive")
        elif choice == "6":
            computer_parts.append("hdmi_cable")

    else:
        print("Please add the following items to the list.")
        for i in available_parts:
            print("{}: {}".format(available_parts.index(i) + 1, i))
    choice = input()

print(computer_parts)
