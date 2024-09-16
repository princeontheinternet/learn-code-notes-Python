# Types Of Errors in Python

* ## SyntaxError

  * It occurs when there is a **problem with the syntax of the code**, such as a missing parenthesis or colon.
  
---

* ## IndentationError

  * It is raised when there is a **problem with the indentation of the code**.
  * According to PEP (Python Enhancement Proposals) ***spaces*** are preferred over tabs for indentation method. We must use ***4 spaces*** per indentation level.

---

* ## NameError
  
  * It is raised when a **variable/function is not defined**.
  
---

* ## TypeError

  * It is raised when an **operation/function is applied to an object/variable of an incompatible data type**.
  * For Eg - 1, you might get a TypeError when trying to **add a string and a number together**.
  * For Eg - 2, ```len(123)``` #int does not have len function as it not indexed.
  * TypeError occurs because of Python being ***strongly typed*** that enforces strict restrictions of intermixing values of different types.

---

* ## IndexError

  * It occurs when trying to access an element in a list or other indexed data structure with an **index that is outside of its valid range**.

---

* ## ValueError

  * It is raised when a built-in operation/function receives an argument with the right type but an inappropriate value, such as passing a string to a function that is expecting an integer.
  * Eg: ```int("hello")``` will raise a ValueError.
  * Eg:

    ```python
    list1 = [1,2,3,4]
    print(list.index(5))

    # As 5 is not present in list1, therefore we will get ValueError.
    ValueError: 5 is not in list
      ```

---

* ## KeyError

  * This occurs when trying to **access a dictionary key that does not exist**.

---

* ## AttributeError

  * It is raised when a **variable/object does not have an attribut/method** that you are trying to access.
  * Eg ```dict.remove()``` will raise AttributeError as dictionaries do not have remove method.

---
