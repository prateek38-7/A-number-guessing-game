import random

while True:

    choice = input("""
Modes:
hard
mid
easy
or exit: """)

    if choice == "exit":
        break

    elif choice == "hard":
        secret_number = random.randint(1, 1000)
        print("Guess a number between 1 and 1000")

    elif choice == "mid":
        secret_number = random.randint(1, 100)
        print("Guess a number between 1 and 100")

    elif choice == "easy":
        secret_number = random.randint(1, 50)
        print("Guess a number between 1 and 50")

    else:
        print("Invalid mode!")
        continue

    while True:
    
    
    
        guess = int(input("Enter your guess: "))

        if guess > secret_number:
           print("High guess")

        elif guess < secret_number:
             print("Low guess")

        else:
             print("Right!")
             break