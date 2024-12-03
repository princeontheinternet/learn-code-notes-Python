# **Function Signature:**

* Function signature means the definition of a function.
* It includes function name and parameter it defines.

## **Print Function:**

### print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

* ***objects**
  * Print zero or more objects.
  
  * We can pass multiple arguments to the print() function, and they are collected as a tuple, separated by commas. The *objects parameter then unpacks these arguments and prints them individually, joined by the value specified in the sep parameter.

    ```python
    print("Hello", "World", 123)  # Prints: Hello World 123
    ```

    ```python
    def my_function(*args): #*args unpacks all
    print(args)     # (1, 2, 3, 'hello', True) --> This is entire Tuple
    print(*args)    # 1 2 3 hello True ---> This is unpacked tuple

    my_function(1, 2, 3, "hello", True) # ----> passing multiple values as argument
    ```

* **sep** --> It is a keyword argument which means separated by.
It defaults to separated by space.
* **end** --> It is a keyword argument which means end with.
It defaults to newline character \n.

* **file**
  * Default: file=sys.stdout.
  
  * Specifies where the output should go. By default, it goes to the console.
  
  * You can redirect the output to a file.
  
    ```python
    with open("output.txt", "w") as f:
    print("Hello, file!", file=f)  # Writes "Hello, file!" to output.txt
    ```

* **flush** --> flush: Default False. Controls when the output buffer is cleared (flushed) and sent to the console or a file.
