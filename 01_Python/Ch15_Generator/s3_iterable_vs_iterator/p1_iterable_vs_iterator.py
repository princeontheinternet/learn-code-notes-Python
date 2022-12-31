# Iterator vs Iterable

"""
Iterable:

    ● Iterable is anything you can loop over with a for loop.
    ● Can be iterated using `for loop`.
    ● Iterable supports iter() function.
    ● It occupies memory as soon as the object is defined or created.
    ● Eg - List, Strings, Range

Iterator:

    ● An iterator is an object which implements the iterator
       which consist of the methods __iter__() and __next__().
    ● Can be iterated using `for loop`.
    ● Iterator supports iter() and next() function
    ● It does not occupy the memory and returns the data one element at a time.
    ● If there are no more elements, __next__() must raise the StopIteration exception.
    ● The for loop will terminate as soon as it catches a StopIteration exception.

"""

# List is an Iterable
l1 = [1, 2, 3, 4, 5, 6]

for i in l1:
    print(i)


# List is also an Iterator
l2 = iter(l1)
print(next(l2))

for i in l2:
    print(i)  # it will start with 2nd element as previous line is using 1st element in next function.



