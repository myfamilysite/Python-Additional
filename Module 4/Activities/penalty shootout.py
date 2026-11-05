import random

def penalty_shootout():
    options = ["TL", "BL", "MD", "TR", "BR"]
    score = 0
    total_rounds = 5

    #Instructions
    print("*" * 50)
    print("⚽ PENALTY SHOOTOUT: STRIKER MODE ⚽\n")
    print(f"Type TL, BL, MD, TR or BR to take your shot.\n")
    print (f"TL = Top-Left")
    print (f"BL = Bottom-Left")
    print (f"MD = Middle")
    print (f"TR = Top-Right")
    print (f"BR = Bottom-Right")    
    print("*" * 50)

    #Loop
    for round_num in range(1, 6):
        print(f"Round {round_num} of {total_rounds}")
        
        # Player takes a shot
        player_shot = input("Where do you want to shoot? ").strip().upper()
        
        # Check if input is valid
        if player_shot not in options:
            print("Invalid choice! You missed your shot.\n")
        else:
            # Goalkeeper picks a random direction
            keeper_direction = random.choice(options)
            
            if keeper_direction == player_shot:
                print(f"❌SAVED! The keeper dived {keeper_direction} and blocked your shot.\n")
            else:
                print(f"👏🏽GOAL! The keeper dived {keeper_direction}, you scored!\n")
                score += 1

    # Final Results
    print("----------------------------------------")
    print(f"FINAL SCORE: You scored {score} out of {total_rounds} goals!")
    print("----------------------------------------")

# Run the game
if __name__ == "__main__":
    while True:
        penalty_shootout()
        restart = input("\nDo you want to play again? (y/n): ").strip().lower()
        if restart == 'n':
            print("Thanks for playing!")
            break


