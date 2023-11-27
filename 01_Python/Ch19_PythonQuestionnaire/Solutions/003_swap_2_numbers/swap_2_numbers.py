
a = 2
b = 3

''' 1. Using Temporary Variable Approach '''
temp = a
a = b
b = temp 

''' Using Unpacking Variables/Tuple Approach '''
a, b = b, a

''' Using Unpacking Variables/Tuple Approach '''
[a, b] = [b, a]


''' Using Arithmetic Operations Approach '''
a = a + b
b = a - b
a = a - b

print(a, b)
