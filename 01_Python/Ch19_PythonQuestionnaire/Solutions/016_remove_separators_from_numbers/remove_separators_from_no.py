number = "9,223:833,329.3928"

separators = ''
new_number = ''

for i in number:
    if i.isnumeric():
        new_number += i
    else:
        separators += i

print(new_number)
print(separators)

