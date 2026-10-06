import random, sys

print("===== Welcome to Rock, Paper, Scissors! =====")

wins = 0
losses = 0
ties = 0

while True:
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
    print("Enter your move: (r)rock, (p)paper, (s)scissors) or '(q)quit' to exit.")
    userMove = input().lower()
    if userMove == "q":
        print("Thanks for playing! Goodbye!")
        sys.exit()
    elif userMove == "r" or userMove == "p" or userMove == "s":
        pass
    else:
        print("Invalid input. Please try again.(r, p, s, or q)")
        continue

    if userMove == "r":
        print("Rock versus...")
    elif userMove == "p":
        print("Paper versus...")
    else:
        print("Scissors versus...")

    computerMove = random.choice(['r', 'p', 's'])
    if computerMove == "r":
        print("Rock!")
    elif computerMove == "p":
        print("Paper!")
    else:
        print("Scissors!")

    if userMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif (userMove == "r" and computerMove == "s") or (userMove == "p" and computerMove == "r") or (userMove == "s" and computerMove == "p"):
        print("You win!")
        wins += 1
    else:
        print("You Lose!")
        losses += 1
