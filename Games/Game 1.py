import random

def vault_cracker():
    secret_code = random.randint(1, 50)
    attempts_left = 5
    
    print("=" * 45)
    print("🕵️‍♂️  WELCOME TO THE VAULT CRACKER CHALLENGE  🕵️‍♀️")
    print("Security System: Secret code generated between 1 and 50.")
    print(f"You have {attempts_left} attempts to crack the code before lock-out!")
    print("=" * 45)

    while attempts_left > 0:
        guess_input = input(f"\n[Attempts Remaining: {attempts_left}] Enter code guess: ").strip()
        
        # Guard clause for invalid non-numeric inputs
        if not guess_input.isdigit():
            print("⚠️ System Warning: Enter digits only!")
            continue
            
        guess = int(guess_input)

        if guess == secret_code:
            print(f"\n🎉 ACCESS GRANTED! You cracked the vault code ({secret_code})! 🔓💰")
            break
        elif guess < secret_code:
            print("📉 TOO LOW! The security frequency is higher.")
        else:
            print("📈 TOO HIGH! The security frequency is lower.")

        attempts_left -= 1

    if attempts_left == 0:
        print(f"\n🚨 SYSTEM LOCKOUT! You ran out of attempts. Secret code was: {secret_code}")

# Run Game
if __name__ == "__main__":
    vault_cracker()