print("Guessing game starting...")
import random

secret_number = random.randint(1, 100)
attempts = 0

print("Guessing game starting...")
print("I have picked a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Correct! You got it!")
        print("The secret number was:", secret_number)
        break
    elif  guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    if attempts == 5:
            print("You lose! You ran out of attempts!")
            print("The secret number was:", secret_number)
            break  
        