""""
Local Scope: Variables declared inside a function are said to have local scope and are only accessible within that function.
When a function is executed, a new local scope is created, and when the function returns or terminates, the local scope is destroyed and all its variables are lost.

Global Scope: Variables declared outside a function have a global scope and are accessible from anywhere in the code.

The concept of local and global applies to variables declared inside functions, 
but do not to variables delared inside control structures, like `if`, `for` or `while`.

Global Constants: 
    - These are values that can be accessed anywhere in the code.
    - It's value is meant to remain unchanged throughout the program.
    - It is written in upper case.
"""

PI = 3.14   # Global Constant: Value cannot be changed
radius = 2  # Global Variable: Value can change


def modifying_global_variable_not_recommended():
    global radius   # if I don't declare global variable and try to change the value of radius directly then I will get error
    radius += 1
    return radius

def modifying_global_variable_recommended():
    return radius + 1   # Here I do not need to declare global variable as I am just using it's value and not changing it's value.


print(radius)
print(modifying_global_variable_not_recommended())
print(modifying_global_variable_recommended())



