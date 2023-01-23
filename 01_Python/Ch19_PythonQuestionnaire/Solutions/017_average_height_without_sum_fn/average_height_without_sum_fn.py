user_heights = input("Input a list of student heights: ")

list_of_heights = user_heights.split(" ")

sum_height = 0
no_of_users = 0

for height in list_of_heights:
    sum_height += int(height)
    no_of_users += 1

average_height = round(sum_height/no_of_users)

print(average_height)