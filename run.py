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

playgame()