def calculate_area(length, width):  # Function name is in the global namespace; parameters are in the local namespace
    area = length * width  # Variable 'area' is created in the local namespace
    print(area)  # Execution and lookup happen via the local namespace

new_area =calculate_area(10, 4)  # Arguments (10, 4) are evaluated in the global namespace and passed to the local parameters
print(new_area)
#print (f"{calculate_area(10,4) * 2}")
