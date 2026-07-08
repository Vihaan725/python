import random
playing = True
number = str(random.randint(0,9))
print("I will generate a number from zero to nine, and you have to guess the number one digit at a time. ")
print("The game ends when you get one hero! ")
while playing:
    guess = input("Give me your best guess \n")
    if number == guess:
        print("You got the number correct!")
        print("The number was", number)
        break
    
    else:
        print("Your guess was not right. Please try again. \n")
