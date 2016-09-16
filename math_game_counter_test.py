#The aim of this code is to make a interactive maths game in using Python
#I may try to create a GUI, depending on the time constraints (5/9/16)

#TO DO: add score changer depending in difficulty_choice
#       Start designing a ttk window (16/9/16)

############ IMPORTS ############
from random import *

############ FUNCTIONS AND CODE ############
def random_numbers(n):
    """This function calculates two random numbers for the arithmatic functions.
        The parameter n is determined by the difficulty choice."""
    num1 = randrange(1, n)
    num2 = randrange(1, n)
    while num1 == num2:
        num2 = randint(1, n)
    return num1, num2

def number_range(difficulty_choice):
    """This function determines the range of the question"""
    if difficulty_choice == "easy":
        number_range = 10
        score_add
    elif difficulty_choice == "medium":
        number_range = 50
    elif difficulty_choice == "hard":
        number_range = 100
    elif difficulty_choice == "expert":
        number_range = 1000
    num1, num2 = random_numbers(number_range)
    return num1, num2

def check_and_tell(guess, answer, score): #definition of the function, takes score as an argument
    if guess == answer:
        score += 10
        return score
        print("Correct! Your score is now {} points".format(score))
    else:
        if score - 5 >= 0:
            score -= 5
            return score
        elif score - 5 < 0:
            score = 0
            return score
        print("Sorry, the answer is {}. Your score is now {} points".format(answer, score))

def add(level):
    num1, num2 = number_range(level)
    answer = num1 + num2
    guess = int(input("What is {} + {}?".format(num1, num2)))
    interim_score = check_and_tell(guess, answer, game_score)
    return interim_score

def subtract(level):
    num1, num2 = number_range(level)
    answer = num1 - num2
    guess = int(input("What is {} - {}?".format(num1, num2)))
    interim_score = check_and_tell(guess, answer, game_score)
    return interim_score

def multiply(level):
    num1, num2 = number_range(level)
    answer = num1 * num2
    guess = int(input("What is {} * {}?".format(num1, num2)))
    interim_score = check_and_tell(guess, answer, game_score)
    return interim_score

def divide(level):
    num1, num2 = number_range(level)
    answer = num1 / num2
    guess = int(input("What is {} / {}?".format(num1, num2)))
    interim_score = check_and_tell(guess, answer, game_score)
    return interim_score

#### GAME #####
play_again_check = True
game_score = 0

name = input("What is your name?")
print("Hi {}.".format(name))

print("This game is a maths game. You will answer questions from addition, subtraction, multiplication and division. A correct answer gives you 10 points, a wrong answer takes away 5.")

while play_again_check == True:
    game_choice = int(input("""Which game would you like to play?
                                1: Addition
                                2: Subtraction
                                3: Multiplication
                                4: Division""").strip())

    level = input("Easy, Medium, Hard, Expert? ").strip().lower()

    if game_choice == 1:
        game_score = add(level)
    elif game_choice == 2:
        game_score = subtract(level)
    elif game_choice == 3:
        game_score = multiply(level)
    elif game_choice == 4:
        game_score = divide(level)

    print(game_score)

    ask = input("Do you want to play again?").strip().lower()
    if ask[0] == "n":
        print("Goodbye")
        play_again_check = False
