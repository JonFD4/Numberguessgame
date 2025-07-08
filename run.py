import random

def playgame():

    """
    Create difficulties levels. If user chooses easy,the random generated will be between 1 and 10 with 5 attempts.
    If user choose hard, random number will be generated between 1 and 50
    If no difficulty is chosen or the wrong character is inputted, it will default to easy
    """
    difficulty = input("Choose your level easy/ hard: ").lower()

    if difficulty == "easy":
        max_number = 10
        attempts = 5
    elif difficulty == "hard":
        max_number = 50
        attempts = 3
    else: 
        print("Invalid difficulty input, default to easy")
        max_number = 10
        attempts = 5

    secret_number = random.randint(1,max_number)
    
    while attempts > 0
        guess = input(f'Guess a number between 1 and {max_number}') 
       
        if not guess.isidigit():  # Validation check to ensure user enters a number
            print(' Please enter a valid number: ')
            continue
       
        guess = int(guess)
        if guess == secret_number:
            print('You guessed it!')
        elif guess > secret_number:
            print('Too big')
        else:
            print('Too small')
        
        attempts-=1

playgame()