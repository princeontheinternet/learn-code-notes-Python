#                   Section 5: Else loop

# Python Else Loop:

#   Python allows else keyword to be used with "for" & "while" loop too.
#   The statement in the else block will be executed after all the iterations are completed.
#   The program exits the loop only after else block is executed.
#   So else block will get executed until you have a break statement which will break the entire loop.

for i in range(5):
    print("iteration {} in for loop".format(i + 1))
else:
    print("else block in loop")
print("Out of the loop")


#   Output:

# iteration 1 in for loop
# iteration 2 in for loop
# iteration 3 in for loop
# iteration 4 in for loop
# iteration 5 in for loop
# else block in loop
# Out of the loop
