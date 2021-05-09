# Default Parameter Value

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
# If we call the function without argument, it uses the default value:
my_function("Brazil")

