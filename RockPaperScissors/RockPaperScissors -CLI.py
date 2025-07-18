import random

def Rules(Choice , Computer):
    if Choice == Computer:
        return "Tie"
    elif Choice == "ROCK":
        if Computer == "PAPER":
            return "Lose"
        elif Computer == "SCISSORS":
            return "Win"
    elif Choice == "PAPER":
        if Computer == "SCISSORS":
            return "Lose"
        elif Computer == "ROCK":
            return "Win"
    elif Choice == "SCISSORS":
        if Computer == "PAPER":
            return "Win"
        elif Computer == "ROCK":
            return "Lose"
    else:
        print("Please Enter a Valid Choice : Rock , Paper, Scissors")
        return None

def Game():
    Player_Points = 0
    Computer_Points = 0
    Play = "Y"
    hands = ["ROCK", "PAPER", "SCISSORS"]
    
    while Play == "Y":
        Choice = input("Enter your choice: Rock, Paper or Scissors: ").upper()
        if Choice not in hands:
            print("Invalid input! Please try again.")
            continue

        Computer = random.choice(hands)
        Result = Rules(Choice , Computer)

        print("Computer chose:", Computer)

        if Result == "Win":
            Player_Points += 1
            print("You won this round, 1 point added to you.")
        elif Result == "Lose":
            Computer_Points += 1
            print("You lost this round, 1 point added to computer.")
        elif Result == "Tie":
            print("This round was a tie, NO point added.")

        Play = input("Do you wish to Continue? Y/N: ").upper()

    return Player_Points, Computer_Points

# Start the Game
print("Welcome to Rock-Paper-Scissors!")
print("Point system")
print("Win : +1")
print("Lose : +1 to computer")
print("Tie : 0")

Player_Points, Computer_Points = Game()

#Final Results
print("\nFinal Score:")
print(f"You: {Player_Points}")
print(f"Computer: {Computer_Points}")

if Player_Points > Computer_Points:
    print("You won the game")
elif Computer_Points > Player_Points:
    print("Computer won the game")
else:
    print("It's a tie")