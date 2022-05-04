from art import logo
import random


LEVEL = {
  "easy": 10,
  "hard": 5
}


def difficulty():
  '''Assigns difficulty level based on user choice.'''
  diff = input("Choose a difficulty: Type \"easy\" or \"hard\" ").lower()
  
  return LEVEL[diff]

def guess_check(player_guess, random_number, guesses_remaining):
  '''Checks the user's guess and decrements if wrong'''
  if player_guess == random_number:
    print("You guessed the number. You win!")
  elif player_guess > random_number:
    print("Too high.")
    return guesses_remaining - 1
  elif player_guess < random_number:
    print("Too low.")
    return guesses_remaining - 1
    

def game():
  print(logo)
  
  random_number = random.randint(1, 100)
  print("I'm thinking of a number between 1 and 100.")

  guesses_remaining = difficulty()
  player_guess = 0
  
  while player_guess != random_number:
    print(f"You have {guesses_remaining} attempts remaining.")
  
    player_guess = int(input("Guess a number: "))
  
    guesses_remaining = guess_check(player_guess, random_number, guesses_remaining)

    if guesses_remaining == 0:
      print("You ran out of guesses. You lose.")
      return
    elif player_guess != random_number:
      print("Guess again.")

  
  
game()
    
