user_height = input("Enter your height in meters: ")
user_weight = input("Enter your weight in kgs")

bmi = float(user_weight)/float(user_height)**2


if bmi < 18.5:              
    print(f"Your BMI is {round(bmi)},  you are underweight")
elif 18.5 < bmi < 25:   # chain comparison 
    print(f"Your BMI is {round(bmi)} you have a normal weight.") 
elif 25 < bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif 30 < bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")



'''
Learnings:

    1. Elif is a group of stmt and it is going to check the first if stmt and only if this fails it will check the next elif one.

'''

# The below code is also correct but it proves our learning.

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")
