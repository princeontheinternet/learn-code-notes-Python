print("Welcome to the Love Calculator!")

person1 = input("What is your name? \n ")
person2 = input("What is their name? \n ")

true = 0
love = 0

for each_char in person1:
    if each_char.lower() in "true":
        true += 1
    if each_char.lower() in "love":
        love += 1

for each_char in person2:
    if each_char.lower() in "true":
        true += 1
    if each_char.lower() in "love":
        love += 1

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
