quote = """Alright but apart from the Sanitation, the Medicine, \
Education, Wine, Public, Order, Irrigation, Roads, the Fresh-Water \
System and Public Health, what have the Romans ever done for us? """

capital_letters = ""

for char in quote:
    if char.isupper():
        print(char)
        capital_letters += char

print(capital_letters)