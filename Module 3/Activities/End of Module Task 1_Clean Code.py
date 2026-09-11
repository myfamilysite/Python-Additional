#start with a variable that will hold our list of test results
results = []

#Instructions
print ("=" * 55)
print("Instructions:\n\nEnter student numerical marks (0-100) for the 4 tests.")
print ("=" * 55)

# Get user data
grade = int(input("Please enter the grade: "))

subject = input("Please enter the subject: ")

student = input("Please enter the student's name and surname: ")

#Use a for loop to get the 4 test results and append them to the results list
for i in range(1, 5):
    marks_input = float(input("Please enter the student's mark for Test 1: ").replace(',', '.'))
    results.append(marks_input)

#Calculate the term average. Use a f string to add the % symbol.
term_average = (f"{sum(results) / len(results)}%")

#Use a key:value pairing to prepare your output. The built-in enumarate function will add a counter to the list
my_dict = {f"Test {i+1}": f"{mark}%" for i, mark in enumerate(results)}

#Print the output you need. The \n will add an additional line space for readability
print (f"\nThese are the results for {student}:")
print (f"\n{subject} Grade{grade} >- {my_dict}, Term Average: {term_average}")
    
              
              