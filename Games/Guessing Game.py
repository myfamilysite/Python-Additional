#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def play_game():
    random_num = random.randint(1, 50)
    attempts = 0
    print("*" * 125)
    print("This is a guessing game. You need to guess a whole number between 1 and 50. You have 5 attempts. Good luck!!")
    print("*" * 125)

    while attempts < 5:
        attempt = int(input("Enter your guess: "))
        if attempt == random_num:
            print(f"\n🥳That is correct. Amazing!!")
            break
        elif attempt < random_num:
            print(f"🫩Too Low")
        else attempt > random_num:
            print(f"🫩Too High")
            continue

        attempts += 1

    print("In life, never give up.")

# Run Game
if __name__ == "__main__":
    while True:
        play_game()
        restart = input("Do you want to play again? (y/n): ").strip().lower()
        if restart != 'y':
            print("Thanks for playing!")
            break


# In[ ]:




