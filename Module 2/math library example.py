import math

# calculate the area of a circle. The formula for the area of a circle is A=πr²

radius = int(input("Enter the value for the radius of the circle: "))

unit = input("Enter the unit of measurement: ") 

area = math.pi * math.pow(radius, 2)

print (f"The area of the circle is {round(area, 3)}{unit}\u00b2") #Unicode \u00b2 gives the power of 2

print (f"The area of the circle is {math.ceil(area)}{unit}\u00b2")

print (f"The area of the circle is {math.floor(area)}{unit}\u00b2")

