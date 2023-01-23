student_scores = input("Input a list os student score separated by space: ")

list_of_scores = student_scores.split()

max_score = 0

for score in list_of_scores:
    if int(score) > max_score:
        max_score = int(score)

print(f"The highest score in class is: {max_score}")