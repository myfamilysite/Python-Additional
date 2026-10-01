# operators = ("+, -, *, /")

print ("*" * 65)

print ('''\nThis is a simple calculator that you can use for adding, subtracting,
multiplying or dividing 2 numbers. For addition use the '+' key,
for subtraction use the '-' key, for multiplication use the '*' key 
and for division use the '/' key on the keyboard.''')

print()
print ("*" * 65)

operator = input("\nPlease enter the operator that you would like to use and press the 'Enter' key. Use only +, -, * or /  : ")

num1 = float(input("\nPlease enter the 1st number and press the 'Enter' key: ").strip())

num2 = float(input("\nPlease enter the 2nd number and press the 'Enter' key: ").strip())

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







