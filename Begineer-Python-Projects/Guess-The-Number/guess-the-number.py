#!/usr/bin/python3

import random

def user_guess(x):
	random_number = random.randint(1, x)
	
	guess = 0

	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))

		if guess<random_number:
			print("Sorry, guess again. Too low.")
		elif guess>random_number:
			print("Sorry, guess again. Too high.")

		

	print(f"\n\nBINGO!!!!!!!, You Got The Secret Number {random_number}\n\n")



#user_guess(10)


def computer_guess(x):
	low = 1
	high = x
	feedback = ''

	while feedback != 'c':
		if low != high:
			guess = random.randint(low,high)
		else:
			guess = low 

		feedback = input(f"Is {guess} too High [h], too Low [l], or correct [c]: ")
		
		if feedback == 'h':
			high = guess-1
		elif feedback == 'l':
			low = guess+1

	print(f"\n\nBINGO!!!!!!!, Computer guessed your number, {guess}, correctly!\n\n")

#computer_guess(10)


def menu():

	while(True):
		print("---------Main Menu----------\n")
		print("[1] Let the computer guess.")
		print("[2] Let the human guess.")
		print("[0] Exit.")
		print("\n--------------------------\n")

		choice = int(input("Enter you choice [1, 2, 0]: "))

		if choice == 1:
			ran = int(input("Enter the high range value: "))
			computer_guess(ran)

		elif choice == 2:
			ran = int(input("Enter the high range value: "))
			user_guess(ran)

		elif choice == 0:
			print("\nBye...\n")
			exit()


menu()
