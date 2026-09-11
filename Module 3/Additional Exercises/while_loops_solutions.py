# While Loops - Solutions

## Problem 1

For each scenario below, decide whether a `for` loop or a `while` loop is the better fit.

Scenarios:
1. Keep asking the user for a phone number until the format is valid.
2. Print each name in a class roster.
3. Keep trying to connect until the internet is back.

For each scenario, write:
- your loop choice (`for` or `while`)
- a one-sentence explanation of why

*Enter your answer here*

### Solution

1) Keep asking the user for a phone number until the format is valid
- while
- We do not know how many invalid phone numbers the user might enter before giving a valid one.

2) Print each name in a class roster
- for
- We already have a known list of names, so we iterate through each item once.

3) Keep trying to connect until the internet is back
- while
- The number of retries is unknown, so we keep looping until the connection works.

## Problem 2

Create a simple login check that keeps prompting until the user enters the correct password.

Use:
- `correct_password = "sunset42"`
- `user_input = ""`

Write a `while` loop that runs while the password is incorrect:
- Prompt the user with `input("Enter password: ")`
- If the password is wrong, print `"Incorrect password. Try again."`

After the loop ends, print `"Access granted!"`.

**Sample output**
```
Enter password: hello
Incorrect password. Try again.
Enter password: 1234
Incorrect password. Try again.
Enter password: sunset42
Access granted!
```
"""

# TODO write your program here

"""### Solution"""

correct_password = "sunset42"
user_input = ""

while user_input != correct_password:
    user_input = input("Enter password: ")

    if user_input != correct_password:
        print("Incorrect password. Try again.")

print("Access granted!")

"""## Problem 3

Rewrite Problem 2 using `while True` and `break`.

Use:
- `correct_password = "sunset42"`

Prompt the user for a password inside the loop:
- `user_input = input("Enter password: ")`
- If the password is correct, print `"Access granted!"` and `break`
- Otherwise, print `"Incorrect password. Try again."`

This practices the `while True` pattern with a clear exit condition.

"""

# TODO write your program here

"""### Solution"""

correct_password = "sunset42"

while True:
    user_input = input("Enter password: ")

    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")