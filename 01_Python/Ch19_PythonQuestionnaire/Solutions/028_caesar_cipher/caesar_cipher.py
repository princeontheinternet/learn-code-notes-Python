from art import logo

# Added a-z 2 times to handle scenario where new_position > len(alphabet)-1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char        # Added this to handle scenarios of (spaces, numbers and symbols) as they will not be encoded/decoded
    
    print(f"Your {cipher_direction}d result is: {end_text} ")


print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26      # Added this to handle scenarios where shift > len(alphabet)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() == "no":
        print("GoodBye!")
        break




"""
    for letter in start_text:
        position = alphabet.index(letter)

        if cipher_direction == "encode":
            new_position = position + shift_amount

            # if new_position > (len(alphabet) - 1):     
            #     # new_position -= len(alphabet)         
            #     new_position = new_position % len(alphabet)

        elif cipher_direction == "decode":
            new_position = position - shift_amount
        end_text += alphabet[new_position]
    print(end_text)


new_position = new_position % len(alphabet): handles 2 scenarios:
    1. When the position + shift_amount exceeds the index in alphabet
               Eg: for when alphabet is z and shift_amount is 3
               position + shift_amount = 28
    
    2. When the shift_amount > 26 i.e. the lenght of the alphabet.

But this method increases the time complexity and the efficient way to do this is on line 30(shift = shift % 26) and add a-z in alphabet list.
line 30(shift = shift % 26) only handles the scenario 2 and to handle scenario 1 we have added a-z char in alphabet list.
"""