import random

def shoot_penalty(round_num: int) -> bool:
    print(f"\n--- ⚽ PENALTY KICK #{round_num} ---")
    print("Where do you want to aim?")
    print("1. Left Corner 👈")
    print("2. Center Straight 🎯")
    print("3. Right Corner 👉")
    
    player_choice = input("Select aim (1, 2, or 3): ").strip()
    directions = {"1": "Left", "2": "Center", "3": "Right"}

    while player_choice not in directions:
        player_choice = input("Invalid target! Pick 1 (Left), 2 (Center), or 3 (Right): ").strip()

    player_direction = directions[player_choice]
    keeper_direction = random.choice(["Left", "Center", "Right"])

    print(f"\nYou strike towards the {player_direction.upper()}...")
    print(f"Goalkeeper dives to the {keeper_direction.upper()}!")

    if player_direction == keeper_direction:
        print("❌ SAVED! The keeper blocked your shot!")
        return False
    else:
        print("⚽ GOAL!!! You hit the back of the net!")
        return True

def start_match():
    print("🏆 WELCOME TO THE COMMUNITY SOCCER SHOOTOUT. YOU HAVE 3 PENALTIES. GOOD LUCK!! 🏆")
    score = 0
    total_shots = 3

    for round_num in range(1, total_shots + 1):
        if shoot_penalty(round_num):
            score += 1

    print("\n" + "=" * 35)
    print(f"🏁 MATCH FINAL SCORE: {score} / {total_shots} Goals")
    
    if score == 3:
        print("🌟 PERFECT SCORE! You're the match MVP!")
        
    elif score >= 1:
        print("👏 GREAT JOB! Solid performance on the pitch.")
        
    else:
        print("👟 HARD LUCK! Back to practice drills.")
    print("=" * 35)

# Run Game
if __name__ == "__main__":
    start_match()