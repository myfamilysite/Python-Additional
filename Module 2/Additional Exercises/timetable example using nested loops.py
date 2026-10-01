subjects = ["Biology", "Maths", "Science", "Geography"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

subjects.append("Accountancy")
print(subjects)

for day in days:
    for subject in subjects:        
        if subject == "Biology" and day == "Tuesday":
            continue
        elif subject == "Maths" and day == "Friday":
            continue
        elif subject == "Geography" and day == "Monday":
            continue
        elif subject == "Science" and day == "Wednesday":
            continue
        elif subject == "Accountancy" and day == "Thursday":
                    continue
        else:
            print (f"{day:10} {subject}")
print()