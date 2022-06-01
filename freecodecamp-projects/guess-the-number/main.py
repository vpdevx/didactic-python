import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_number:
            print("sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
    
    print(f"Right choice! Congrats. The random number was {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: guess = low
        feedback = input(f"Is {guess} too high(h), too loow(l) or corrently (c)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"YEAH! THE COMPUTEER GUESSED YOUR NUMBER {guess}")

computer_guess(1000)