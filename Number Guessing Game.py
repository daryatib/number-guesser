import random
import time

point = []
def play_game(difficulty):
    attempt = 10 if difficulty == '1' else (5 if difficulty == '2' else 3)
    level = 'Easy' if difficulty == '1' else ('Medium' if difficulty == '2' else 'Hard')

    print ('Great! You have selected the ' + level + ' difficulty level')
    print('Lets start the game!')
    a = random.randint(1, 100)

    start_time = time.time()

    while attempt>0:
        while True:
            guess_input = input('Enter your guess: ')
            if guess_input.isdigit():
                guess = int(guess_input)
                break
            print("Please enter a number!")

        if a==guess :
            end_time = time.time()
            score = (10 if difficulty == '1' else 5 if difficulty == '2' else 3) - (attempt - 1)
            print ('Congratulations! You guessed the correct number in ' + str(score) + ' attempts.')
            print('Time:', round(end_time - start_time, 2), 'seconds')
            point.append(score)
            break
        else:
            print('Incorrect! The number is ' + ('greater' if a>guess else 'less')+  ' than ' + str(guess))
            attempt-=1
    if attempt==0:
        end_time = time.time()
        print('Game over! The number was', a)
        print('Total time:', round(end_time - start_time, 2), 'seconds')

def main():
    print('Welcome to the Number Guessing Game! \nIm thinking of a number between 1 and 100. \nYou have chances to guess the correct number. ')

    while True:
        print('Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)')
        difficulty = input('Enter your choice: ')

        while difficulty not in ('1','2','3')  :
            print ("Please enter 1, 2 or 3!")
            difficulty = input('Enter your choice: ')
        if difficulty in ('1','2','3'):
            play_game(difficulty)

        again = input('Do you want play again? (yes/no): ')
        if again != 'yes':
            print ('The best point was ' + str(min(point) if len(point)!=0 else 0))
            break

if __name__ == "__main__":
    main()
