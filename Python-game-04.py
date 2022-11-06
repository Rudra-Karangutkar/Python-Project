import random
n = random.randrange(1,10)
guess = int(input("Enter any number:\n"))
while n!= guess:
    if guess < n :
        print("Too low")
        guess = int(input("Enter any number again:\n"))
    elif guess > n :
        print("Too high!")
        guess = int(input("Enter any number again:\n"))
    else:
        break
print("Guessed it right!!")