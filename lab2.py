#secret_number=90
secret_number = int(input("Set the secret number (hidden from the guesser): "))

print("\n" + "-"*40)
print("The guessing game begins!")
print("-"*40)

while True:
    guess=int(input("Enter the guess"))

    if guess>secret_number:
        print("Too high! Try again")
    elif guess < secret_number:
        print("Too low! Try again")
    else:
        print("Congratulations")
        break