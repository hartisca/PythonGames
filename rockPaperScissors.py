import random

emoji_map = {
  "rock": "\u270A",
  "paper": "\u270B",
  "scissors": "\u270C"
}

choices = ["rock", "paper", "scissors"]

win_map = {
  "rock": "scissors",
  "scissors": "paper",
  "paper": "rock"
}

player = 0
computer = 0

def jugar():
  global player, computer
  
  while True:
    yourChoice = input('What\'s your next move? ').lower()
    if yourChoice not in choices:
      print('You have to choose between rock, paper, or scissors!')
    else:
      break
  
  machineChoice = random.choice(choices)
  
  print(f"You choose: {emoji_map[yourChoice]} and computer chose: {emoji_map[machineChoice]}")
  
  if yourChoice == machineChoice:
      print("It's a tie!")
  elif win_map[yourChoice] == machineChoice:
      print("You win!")
      player += 1
  else:
      print("You lose!")
      computer += 1

  print(f"Score - You: {player} | Computer: {computer}")

while player < 3 and computer < 3:
  jugar()
  if player == 3 and computer == 3:
    winner = "You won the game!" if player == 3 else "You lost the game."
    print (winner)