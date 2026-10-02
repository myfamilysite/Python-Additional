def calculate_area(length, width):  # Function name is in the global namespace; parameters are in the local namespace
    area = length * width  # Variable 'area' is created in the local namespace
    return area  # Passes the value back; the returned value itself is caught by the global variable


outside_area = calculate_area(10, 4)  # Function call and variable 'outside_area' are in the global namespace

print(outside_area)