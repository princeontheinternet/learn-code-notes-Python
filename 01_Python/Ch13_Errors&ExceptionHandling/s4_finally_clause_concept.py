# FINALLY: The finally block lets you execute code, regardless of the result of the try and except blocks.

x = 10

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
    print("The 'try except' is finished")

print("The 'try except' is finished")

# Even if I don't put finally and just put the above print stmt then also code will exeute.


# ------------------------------------------------------------------------------------------------



def func1():

    try:
        l = [1,2,3,4,]
        user_input = int(input("Enter the index: "))
        print(l[user_input])
        return "Valid Index"
    except:
        print("Some error occurred")
        return "Invalid Index"
    finally:
        print("I am always executed")
    print("Am I always executed?") 
    # This will not executed because try and except are returning back but finally clause wll get executed in any case
    

x = func1()
print(x)

