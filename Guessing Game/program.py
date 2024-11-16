from functions import UserGuess


def play_game():

    random_number = UserGuess.generate_number() #put the generated random number in variable.
    attempt = 1 # attempt for how many tries it takes for the guesser to geuss the correct number.
    
    while True:
        user_input = input('Enter your guess (1-100): ')
        
        if not UserGuess.is_user_input_digit(user_input): # checking and validate the user if it is digit and no characters inluded.
            print("Invalid input. Please enter a number not characters or dont include one in your input.")
            continue
        if not UserGuess.is_user_input_in_range(user_input): #checking and validate the user input if is numbers between 0 - 101. 
            print("Invalid Input. Please enter a number between 0 and 101.")
            continue
        if UserGuess.is_user_guess_the_number(user_input, random_number): # checking if the user guessed the random number.
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempt} attempts.")
            break
        # if the user didn't guess the random number correctly, this will check if the guess is higher or lower than the generated number.
        if UserGuess.is_user_input_is_greater(user_input,random_number):
            print(f"Wrong! Your guess of {user_input} is high. Try a lower number.")
        else:
            print(f"Wrong! Your guess of {user_input} is low. Try a higher number.")
        
        attempt += 1 # iterate until the user guess the number correctly,it will be used for prompting on how many tries it would take for the user to guess corerectly.

if __name__ == "__main__":
    play_game()