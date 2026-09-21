# Module 7 - Activity

class InvalidValueError(Exception):
    """Custom exception raised for out-of-range inputs."""
    pass

def process_positive_number(user_input: str) -> float:
    try:
        value = float(user_input)
        if value <= 0:
            raise InvalidValueError("Number must be greater than zero.")
    except ValueError:
        print("Error: Conversion failed. Input is not a valid number.")
        return 0.0
    except InvalidValueError as custom_err:
        print(f"Custom Error: {custom_err}")
        return 0.0
    else:
        print("Parsing successful.")
        return value
    finally:
        print("Execution of input processor completed.")

# Testing different scenarios
print("Test 1 (Valid Input):")
res1 = process_positive_number("45.5")

print("\nTest 2 (Non-numeric Input):")
res2 = process_positive_number("abc")

print("\nTest 3 (Negative Input):")
res3 = process_positive_number("-10")