import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range == 0:
        print("Please type a number large than 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")

# import random
#
# number_input = input("Enter a random number : ")
#
# if number_input.isdigit():
#     number_input = int(number_input)
# else:
#     quit()
#
# number_random = random.randint(0, number_input)
#
# guesess = 0
# while True:
#     guesess += 1
#     number = input("Enter a number : ")
#     number = int(number)
#     if number == number_random:
#         print("You are Correct!")
#         break
#     elif number > number_random:
#         print("Your number above the random number")
#         continue
#     else:
#         print("Your number below the random number")
#         continue
#
# print("Your guesess", guesess, "trying")