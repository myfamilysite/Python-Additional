operators = ("+, -, *, /")

print ("This is a calculator that you can use for ") 
print ("adding, subtracting, multiplying or dividing 2 numbers.")

operator = input("\nPlease enter the operator that you would like to use. Use only +, -, * or /.")

num1 = float(input("\nPlease enter the 1st number: "))
num2 = float(input("\nPlease enter the 2nd number: "))

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1/num2

if operator == "+":
    print (add)

elif operator == "/":
    print (round(divide ,3))

elif operator == "*":
    print (multiply)

elif operator == "-":
    print (subtract)

else:
    print (f"{operator} is not a valid operator")







