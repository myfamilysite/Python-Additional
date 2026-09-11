import random

def play_game():
    random_num = random.randint(1, 50)

    print("*" * 60)
    print("Guess a whole number between 1 and 50. You have 5 attempts!")
    print("*" * 60)

    for attempt_num in range(1, 6):           # attempt_num = 1, 2, 3, 4, 5
        guess = int(input(f"Attempt {attempt_num}: Enter your guess: "))

        if guess == random_num:
            print(f"\n🥳 That is correct! Amazing!!")
            break
        elif guess < random_num:
            print(f"🫩 Too Low! {5 - attempt_num} attempts remaining.")
        else:
            print(f"🫩 Too High! {5 - attempt_num} attempts remaining.")

    else:
        # Only runs if the loop ended WITHOUT a break (no correct guess)
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