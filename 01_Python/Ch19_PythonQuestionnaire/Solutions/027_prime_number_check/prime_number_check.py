def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if (number%i) == 0:
            is_prime = False

    if is_prime:
        print(f"{number} a prime number")
    else:
        print(f"{number} not a prime number")
            

user_number = int(input("Enter a number: "))
prime_checker(number=user_number)