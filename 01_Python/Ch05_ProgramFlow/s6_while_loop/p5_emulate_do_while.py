# A Do while loop is a loop that executes the body of the loop atleast once before checking the condition that is present at the end.

# A do while state can be achieved in Python with the help of below code.

n=0
while True:
    n += 1
    print(n)
    if n >= 5:
        break

print("*" * 80)

while True:
    number = int(input("Enter a negative number to break throuh the program: "))
    print(number)
    if not number >= 0:
         break

#   Output:
# 1
# 2
# 3
# 4
# 5