subjects = ["Biology", "Maths", "Science", "Geography", "Accountancy"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print ("Training at Science Park")
for index, (subject,day) in enumerate(zip(subjects,days), start=1):
    print (f"{index}. {day:10} {subject}")
