import random

def play_game():
    random_num = random.randint(1, 50)
    attempts = 0

    print("*" * 60)
    print("Guess a whole number between 1 and 50. You have 5 attempts!")
    print("*" * 60)

    while attempts < 5:
        attempt = int(input("Enter your guess: "))

        if attempt == random_num:
            print(f"\n🥳 That is correct! Amazing!!")
            break
        elif attempt < random_num:
            attempts += 1
            print(f"🫩 Too Low! {5 - attempts} attempts remaining.")
        else:
            attempts += 1
            print(f"🫩 Too High! {5 - attempts} attempts remaining.")

    else:
        # This runs only if the while loop finished WITHOUT a break
        print(f"\n😔 Out of attempts! The number was {random_num}.")

    print("In life, never give up. 💪")

# Run Game
if __name__ == "__main__":
    while True:
        play_game()
        restart = input("\nDo you want to play again? (y/n): ").strip().lower()
        if restart != 'y':
            print("Thanks for playing!")
            break