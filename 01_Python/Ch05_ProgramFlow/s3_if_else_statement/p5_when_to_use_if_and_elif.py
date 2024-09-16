# WAP based on a user's order, work out their final bill

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill +=15
elif size == "M":       # Here we are using elif and not if: Check Learning section below
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1


# Learning

# - if: Checks every condition independently, even if earlier ones are true. Use it when more than one condition can be true at the same time.
# - elif: Stops checking once one condition is true. Use it when only one condition can be true, making the code more efficient.