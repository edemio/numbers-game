from random import randint

random_int = randint(1, 100)
my_guess = 0
tries = 0
while my_guess != random_int:
    my_guess = int(input('guess a random number between 1 and 100: '))
    if my_guess == random_int:
        print(f'you guessed {random_int} correctly whoop whoop!!')
        print()
    else:
        print(f'oops {my_guess} is not the number we are looking for')
        if my_guess < random_int:
            print(f'your guess ({my_guess}) is too low, please try again.')
        else:
            print(f'your guess ({my_guess}) is too high, please try again!')
    tries += 1
print(f'it took you {tries} tries to guess {random_int} correctly!')
