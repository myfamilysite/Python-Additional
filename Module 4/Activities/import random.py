import random

low = 1
high = 100

attempts = 0

number = random.randint(low, high)

while True:
    
    guess = int(input('Guess a number between 1 and 100: '))    
    attempts = attempts+1
    print (f"You have used {attempts} attempts")

    if guess == number:
        print ('Awesome!! You guessed the number')
        break

    elif guess < number:
        print ('Too low')
        
    else:
        print ('Too high')
        
    