# Using count string method

print("Welcome to the Love Calculator!")

person1 = input("What is your name? \n ")
person2 = input("What is their name? \n ")

true = 0
love = 0

combined_name = person1.lower() + person2.lower()

for i in "true":
    true += combined_name.count(i)

for i in "love":
    love += combined_name.count(i)

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
