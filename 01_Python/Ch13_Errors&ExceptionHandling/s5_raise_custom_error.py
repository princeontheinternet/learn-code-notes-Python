a = int(input("Enter a number between 5 & 9: "))

if not 5<=a<=9:
    raise ValueError(f"{a} is not between 5 and 9")
