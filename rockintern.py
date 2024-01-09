import random

while True:
    user_choice = int(input("What do you choose? 1 for rock, 2 for scissors, 3 for paper: "))
    computer_choice = random.randint(1, 3)
    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 3 and computer_choice == 2 or user_choice == 2 and computer_choice == 1 or user_choice == 1 and computer_choice == 3:
        print("Computer wins!")
    else:
        print("You win!")
    
    next_play = input("Let's play again? (yes/no): ")
    if next_play.lower() != "yes":
        break