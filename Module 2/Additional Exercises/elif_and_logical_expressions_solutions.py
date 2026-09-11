# `elif` and Logical Expressions - Solutions

## Problem 1
Given a test score, determine and print the letter grade using this scale:
- 90 and above: "A"
- 80-89: "B"
- 70-79: "C"
- 60-69: "D"
- Below 60: "F"

**Sample output**
```
score = 85
B

score = 62
D
```
"""

# TODO write the grade classifier
score = 85

"""### Solution"""

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

"""## Problem 2
A roller coaster has two requirements: riders must be at least 48 inches tall and at least 12 years old. Given a rider's height in inches and their age, print "You can ride!" if they meet both requirements. Otherwise, print "Sorry, you don't meet the height or age requirement."

**Sample output**
```
height_inches = 52, age = 14
You can ride!

height_inches = 45, age = 14
Sorry, you don't meet the height or age requirement.
```
"""

# TODO write the ride eligibility checker
height_inches = 52
age = 14

"""### Solution"""

height_inches = 52
age = 14

if height_inches >= 48 and age >= 12:
    print("You can ride!")
else:
    print("Sorry, you don't meet the height or age requirement.")

"""## Problem 3
Write a program that suggests an outdoor activity based on the weather. Given a temperature in degrees Fahrenheit and whether it is raining, print a recommendation using these rules:
- If it's not raining and the temperature is 65 or above: print "Great day for a picnic!"
- If it's raining or the temperature is below 32: print "Stay indoors. Not a great day to be outside."
- Otherwise: print "A decent enough day for a short walk."

**Sample output**
```
temperature = 72, is_raining = False
Great day for a picnic!

temperature = 28, is_raining = True
Stay indoors. Not a great day to be outside.

temperature = 55, is_raining = False
A decent enough day for a short walk.
```
"""

# TODO write the outdoor activity recommender
temperature = 72
is_raining = False

"""### Solution"""

temperature = 72
is_raining = False

if not is_raining and temperature >= 65:
    print("Great day for a picnic!")
elif is_raining or temperature < 32:
    print("Stay indoors. Not a great day to be outside.")
else:
    print("A decent enough day for a short walk.")