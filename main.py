import random

def game1():
  def game():
    controlls = input("Use keyboard to type / press enter to send message and continue ")
    
    name = input("What is your name?: ")
    
    
    print("Hello "+name)
    
    
    Game = input("Lets play a game, press Enter ")
    
    print()
    print()
    print()
    print()
    print()
    
    
    
    
    print("Winning Rules of the Rock paper scissor game as follows: \n"
                                    +"Rock vs paper->paper wins \n"
                                    + "Rock vs scissor->Rock wins \n"
                                    +"paper vs scissor->scissor wins \n")
    
    print("Ok Lets play")
    
    userChoice = input("pick (rock, paper, scissors) *make sure to put all lowercase: ")
    
    choices_for_computer_to_choose = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choices_for_computer_to_choose)
    print()
    print()
    print()
    print()
    print()
    print()
    
    print(f"{name} you choose {userChoice} and the computer choose {computerChoice} ") 
    
    
    if userChoice == computerChoice:
      print(" It's a tie!")
    elif userChoice == "rock":
      if computerChoice == "scissors":
        print("Rock smashes scissors! You win!")
      else:
        print("Paper covers rock! You lose.")
    elif userChoice == "paper":
      if computerChoice == "rock":
        print("Paper covers rock! You win!")
      else:
        print("Scissors cuts paper! You lose.")
    elif userChoice == "scissors":
      if computerChoice == "paper":
        print("Scissors cuts paper! You win!")
      else:
        print("Rock smashes scissors! You lose.")
  
  game()

  
  name = input("Before You choose if you want to play again what is your name again : ")

  
  play_again = input("Do You Want To Play Again y/n ")



  
  
  if play_again == ("y"):
    print()
    print()
    print()
    print()
    game1()
  
  if play_again == ("n"):
    print(f"Thanks For Playing {name}")

game1()
    
      
    
    
