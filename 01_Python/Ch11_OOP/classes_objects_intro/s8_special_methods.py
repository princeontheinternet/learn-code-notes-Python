# Special Methods

class Book:

    def __init__(self, title , author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        return "A book object has been Deleted"


Python = Book("Python Rocks", "Cazpian Rabs", 200)

print(Python)
print(len(Python))
# del Python

print(Python.author)    # error


