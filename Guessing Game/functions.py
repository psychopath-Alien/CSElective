import random

class UserGuess:
    @staticmethod
    def generate_number(): #fucntion for generating numbers from 1 to 100, return the generated number.
        return random.randint(1, 100)
    
    @staticmethod
    def is_user_input_in_range(user_input): #function for checking the user input and return true if it is from 1 to 100, otherwise it will return false.
        return 1 <= int(user_input) <= 100
    
    @staticmethod
    def is_user_input_digit(user_input): # function for checking the user input if it is digit and return true.
        return user_input.isdigit()

    @staticmethod
    def is_user_guess_the_number(user_input, rand_num): #function for checking if the user guess the number and return true.
        return int(user_input) == rand_num
    
    @staticmethod
    def is_user_input_is_greater(user_input, rand_num): # function for checking if the user input is higher than the random number and true, otherwise false.
        return int(user_input) > rand_num
