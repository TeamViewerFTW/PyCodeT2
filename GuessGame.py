import random

guessesTaken = 0

print('Hello there! What is your name?')
myName = input()

number = random.randint(1,100)
print('Well,' + myName + ',I am thinking of a number between 1 and 100.')
while guessesTaken < 20:
    print ("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print ("Your guess is too low.")

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guesses my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + '.')
    
    
