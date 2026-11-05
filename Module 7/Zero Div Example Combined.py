try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    quotient = numerator / denominator
    print(f"The result is: {quotient}")
    
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}.")
    