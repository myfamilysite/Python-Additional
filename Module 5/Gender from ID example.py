def determine_gender():
    # Get ID number from user input
    id_number = input("Enter your 13-digit ID number: ").strip()

    # Validate that the input is 13 digits long and numeric
    if not id_number.isdigit() or len(id_number) != 13:
        print("Invalid input. Please ensure you enter exactly 13 digits.")
        return

    # Slicing: Python uses 0-based indexing.
    # Digits 7 to 10 correspond to indices 6 up to 10 (exclusive).
    gender_digits_str = id_number[6:10]
    gender_code = int(gender_digits_str)

    # Determine gender based on the 5000 threshold
    if gender_code >= 5000:
        gender = "Male"
    else:
        gender = "Female"

    print(f"\nExtracted gender code: {gender_digits_str}")
    print(f"Determined Gender: {gender}")


# Run the program
determine_gender()