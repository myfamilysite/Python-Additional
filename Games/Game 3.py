# Module 4 Game: Rap Battle Arena

def calculate_hype(word_count: int, exclamation_marks: int) -> int:
    """Calculates crowd hype score based on length and punctuation."""
    base_score = word_count * 5
    multiplier = exclamation_marks * 10
    return base_score + multiplier

# Lambda function for quick bonus score check
is_fire = lambda score: "🔥 ABSOLUTE HIT! 🔥" if score >= 50 else "🧊 Needs more energy! 🧊"

def battle_round(round_name: str):
    print(f"\n--- 🎤 ROUND: {round_name.upper()} ---")
    bar = input("Drop your bars/lyrics: ").strip()
    
    # Process inputs for the function
    words = len(bar.split())
    exclamations = bar.count("!")
    
    score = calculate_hype(words, exclamations)
    verdict = is_fire(score)
    
    print(f"Stats -> Words: {words} | Hype Points: {score}")
    print(f"Crowd Reaction: {verdict}")
    return score

def run_rap_battle():
    print("🏆 WELCOME TO THE COMMUNITY CYPHER RAP BATTLE 🏆")
    
    round1_score = battle_round("Flow Check")
    round2_score = battle_round("Punchline Knockout")
    
    total_score = round1_score + round2_score
    print("\n" + "=" * 40)
    print(f"👑 BATTLE FINISHED! Total Hype Score: {total_score}")
    
    if total_score >= 120:
        print("Legendary performance! You won the cypher trophy! 🥇")
    else:
        print("Good effort! Keep practicing your flow on the mic. 🎧")
    print("=" * 40)

if __name__ == "__main__":
    run_rap_battle()