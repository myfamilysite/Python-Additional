results = []

print ("=" * 55)
print("Instructions:\n\nEnter student numerical marks (0-100) for the 4 tests.")
print ("=" * 55)

grade = int(input("Please enter the grade: "))

subject = input("Please enter the subject: ")

student = input("Please enter the student's name and surname: ")

for i in range(1, 5):
    marks_input = float(input("Please enter the student's mark for Test 1: ").replace(',', '.'))
    results.append(marks_input)
#test1_marks = float(input("Please enter the student's mark for Test 1: ").replace(',', '.'))
#results.append(test1_marks)

#test2_marks = float(input("Please enter the student's mark for Test 2: ").replace(',', '.'))
#results.append(test2_marks)

#test3_marks = float(input("Please enter the student's mark for Test 3: ").replace(',', '.'))
#results.append(test3_marks)

#test4_marks = float(input("Please enter the student's mark for Test 4: ").replace(',', '.'))
#results.append(test4_marks)

term_average = (f"{sum(results) / len(results)}%")

my_dict = {f"Test {i+1}": f"{mark}%" for i, mark in enumerate(results)}

print (f"\nThese are the results for {student}:")
print (f"\n{subject} Grade{grade} >- {my_dict}, Term Average{term_average}")
    
              
              