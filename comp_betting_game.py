from random import randint
import matplotlib.pyplot as plt
import time
import sys
import random


def comp_number_guessing():
    tries = 1
    print('please choose a range for your guessing game:')
    lower_bound = int(input())
    upper_bound = int(input())
    print(f'edem, please pick a number between {lower_bound} an {upper_bound}:')
    my_number = int(input())
    try_list = []
    guessed_numbers = []
    comp_guess = randint(lower_bound, upper_bound)
    while my_number != comp_guess:
        comp_guess = randint(lower_bound, upper_bound)
        guessed_numbers.append(comp_guess)
        if my_number == comp_guess:
            print()
            print(f'you guessed my number {my_number} correctly whoop whoop :)')
        else:
            print(f'unfortunately {comp_guess} was wrong:(')
            if comp_guess < my_number:
                print(f'{comp_guess} is too low please try again.')
                lower_bound = comp_guess + 1
            else:
                print(f'{comp_guess} is too high, please try again.')
                upper_bound = comp_guess - 1
        tries += 1
        try_list.append(tries)
    print(f'it only took you {tries} tries!')
    plt.scatter(try_list, guessed_numbers)
    plt.xlabel('tries')
    plt.ylabel('guessed number')
    plt.show()
    print()
    print('Do you wanna try again? Please enter (y) for yes and (n) for no.')
    question = str(input())
    if question == 'y':
        print('as you wish...')
        print('Before we start. Do you wanna make things a little more interesting? [y] or [n]')
        if str(input()) == 'y':
            print('very well..')
            print(bet())
        if str(input()) == 'n':
            print(comp_number_guessing())
    if question == 'n':
        print('too bad :(, see u next time.')


def bet():
    comp_account = 10
    my_account = 10
    tries = 1
    explanation = f'The game is simple. You must guess how many tries the computer needs to guess your number.\n'\
                   'If your guess is exactly on point you get 5 points (P). If your guess is wrong by only one number\n'\
                   'you get 2 points. But if you guess wrong by more than 2 numbers you will loose 3 points.\n' \
                   'The points you get will be taken from the computers account and vice versa.\n'\
                   f'You and the computer start with {my_account} Points each'
    for character in explanation:
        pause = random.uniform(0.01, 0.03)
        sys.stdout.write(character)
        time.sleep(pause)
    print()
    print("let's begin!")
    print()
    print('This time the games range will be chosen randomly :):')
    while my_account >= 0 and comp_account >= 0:
        lower_bound = 1
        upper_bound = randint(10, 11)
        print(f'Now, please pick a number between {lower_bound} and {upper_bound}:')
        my_number = int(input())
        print('Now guess how many tries the computer may need')
        bet_guess = int(input())
        try_list = []
        guessed_numbers = []
        comp_guess = randint(lower_bound, upper_bound)
        while my_number != comp_guess:
            comp_guess = randint(lower_bound, upper_bound)
            guessed_numbers.append(comp_guess)
            if my_number == comp_guess:
                try_list.append(tries)
                print()
                print(f'The computer guessed your number {my_number} correctly after {tries} tries. :)')
                print("let's take a look at the score...")
                print()
                if bet_guess == tries:
                    my_account += 5
                    comp_account -= 5
                    print('Wow that was on point!!')
                    print()
                    print(f'your account : {my_account}')
                    print(f'computer account : {comp_account}')
                elif bet_guess == tries - 1:
                    my_account += 2
                    comp_account -= 2
                    print('Nice guess!')
                    print()
                    print(f'your account : {my_account}')
                    print(f'computer account : {comp_account}')
                elif bet_guess == tries + 1:
                    my_account += 2
                    comp_account -= 2
                    print('Nice guess!')
                    print()
                    print(f'your account : {my_account}')
                    print(f'computer account : {comp_account}')
                elif bet_guess == tries + 2 | -2:
                    print('Lucky you!')
                    print()
                    print(f'your account : {my_account}')
                    print(f'computer account : {comp_account}')
                elif bet_guess != tries:
                    print('ohh too bad..')
                    my_account -= 3
                    comp_account += 3
                    print(f'your account : {my_account}')
                    print(f'computer account : {comp_account}')
                tries = 1
            else:
                if comp_guess < my_number:
                    print(f'Unfortunately {comp_guess} is too low please try again.')
                    lower_bound = comp_guess + 1
                else:
                    print(f'Unfortunately {comp_guess} is too high, please try again.')
                    upper_bound = comp_guess - 1
            tries += 1
            print()
    print(f'Your final account is: {my_account}')
    print()
    print(f'The computers final score is: {comp_account}')
    if comp_account > 0:
        print()
        print('oh poor you! Next time it will be better!')
    if my_account > 0:
        print('Wow nice work ;)!')
    if comp_account < 0:
        print()
        print("Wow you destroyed him. He's even in debt now!")
        print()
        print("comp: 'I cannot accept that. I am challenging you for a rematch \n" 
              "Do you accept? [y] or [n]")
        if str(input()) == 'y':
            print(bet())
        if str(input()) == 'n':
            print('Too bad, see you next time')
    if my_account < 0:
        print()
        print("Damn you got destroyed. Now you're in debt!")
    print('This game was fun!')
    print()
    print('Wanna go again? [y] or [n]')
    if str(input()) == 'y':
        print(bet())
    if str(input()) == 'n':
        print('Have a nice day!')
