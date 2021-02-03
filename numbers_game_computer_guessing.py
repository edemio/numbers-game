from random import randint
import matplotlib.pyplot as plt

tries = 0
print('please choose a range for your guessing game:')
x = int(input())
y = int(input())
print(f'edem, please pick a number between {x} an {y}:')
my_number = int(input())
try_list = []
guessed_numbers = []
comp_guess = randint(x, y)
while my_number != comp_guess:
    comp_guess = randint(x, y)
    guessed_numbers.append(comp_guess)
    if my_number == comp_guess:
        print()
        print(f'you guessed my number {my_number} correctly whoop whoop :)')
        print(f'it only took you {tries} tries!')
    else:
        print(f'unfortunately {comp_guess} was wrong:(')
        if comp_guess < my_number:
            print(f'{comp_guess} is too low please try again.')
            x = comp_guess + 1
        else:
            print(f'{comp_guess} is too high, please try again.')
            y = comp_guess - 1
    tries += 1
    try_list.append(tries)
plt.scatter(try_list, guessed_numbers)
plt.xlabel('tries')
plt.ylabel('guessed number')
plt.show()

