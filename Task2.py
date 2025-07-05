import random

max_number = input("Type a number: ")

if max_number.isdigit():
    max_number = int(max_number)
    
    if max_number <= 0:
        print("please type a number larger than 0 next time.")
        quit()
else: 
    print("please type a number larger than 0 next time.")
    quit()

r = random.randint(0, max_number)
guesses = 0

while True:
    guesses += 1
    lets_guess = input("make a guess: ")
    if lets_guess.isdigit():
        lets_guess = int(lets_guess)
    else: 
        print("please type a number larger than 0 next time.")
        continue
    
    if lets_guess == r:
        print("you got it!")
        break
    elif lets_guess > r:
        print("you were above the number!")
    else:
        print("you were below the number!")
        
print("You got it in", guesses, "guesses")