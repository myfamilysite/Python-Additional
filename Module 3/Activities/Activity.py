# Module 3 - Activity

grades = []

print("Enter student numerical grades (0-100). Type -1 to finish.")

while True:
    score = float(input("Enter score: "))
    
    if score == -1:
        break
    
    if score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
        continue
        
    grades.append(score)

print("\n--- Processing Grade Results ---")
for index, score in enumerate(grades, start=1):
    if score >= 75:
        category = "Distinction"
    elif score >= 50:
        category = "Pass"
    else:
        category = "Fail"
        
    print(f"Student {index}: Score = {score} -> Result: {category}")