import random

def get_number(prompt, min_val, max_val):
  while True:
    try:
      number = int(input(prompt))
      if min_val <= number <= max_val:
        return number
      else:
        print(f"Please enter a number between {min_val} and {max_val}.")
    except ValueError:
      print("Please enter a valid integer.")


win = False
game_over = False
round = 1
range = int(input('Chose one number range to make your guess, from 1 to: '))

randomNum = random.randint(1, range)

while win == False and not game_over:
    guess = get_number('Make your guess: ', 1, range)
    if guess == randomNum:
        print("That's it! You win!")
        win = True
    elif round == 5:
        print("You had only 5 trys, you lost!")
        game_over = True   
    else:
        print(f"Wrong answer, try a lower number!" if guess > randomNum else "Wrong answer, try a higher number!")
        round += 1