# WAP to print all nos from 0 to 100 divisible by 7.

for i in range(0, 101, 7):        # using range function to print i
    print(i)                      # This is for loop with step

print("*" * 80)

for i in range(0, 101):
    if i % 7 == 0:              # using "Modulus" Arithmetic Operator
        print(i)

print("*" * 80)


for i in range(101)[::7]:       # using slicing
    print(i)


#   Output:

# 0
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70
# 77
# 84
# 91
# 98
# ********************************************************************************
# 0
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70
# 77
# 84
# 91
# 98
# ********************************************************************************
# 0
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70
# 77
# 84
# 91
# 98
