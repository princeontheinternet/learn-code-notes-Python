print("***** Bill Calculator ********")

total_bill = input("Enter total bill: ")
tip_percentage = input("What percentage tip would you like to give? 5, 10, 15? ")
total_people = input("How many people to split the bill? ")

total_bill_with_tip = float(total_bill) + float(tip_percentage)/100 * float(total_bill)

each_person_price = round(total_bill_with_tip/int(total_people), 2)     # if nunber is 33.30, it will display 33.3, therefore we will have to format this

print("Each person should pay Rs {:.2f}".format(each_person_price))



'''
Learnings:

1. round(bill, 2) does the rounding but does not display the result upto 2 decimal places and that's why we have to use string formatting i.e. {:.2f}.bill
'''