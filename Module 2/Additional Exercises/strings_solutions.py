# Strings - Solutions

## Problem 1

Use `print()` to display each of the following. Choose the right type of quotes for each one.

- `Hello, world!`
- `It's a great day`
- `She said "wow!"`

**Sample output**
```
Hello, world!
It's a great day
She said "wow!"
```
"""

# TODO: Print the three strings

"""### Solution"""

print("Hello, world!")
print("It's a great day")
print('She said "wow!"')

"""## Problem 2

For each expression below, predict what it will output — or whether it will cause an error. Then run each one to check.

```python
print("3" + "7")
print(3 + 7)
print("Hello" + " " + "world")
print("5" + 5)
```
"""

print("3" + "7")
print(3 + 7)
print("Hello" + " " + "world")
print("5" + 5)

"""### Solution"""

print("3" + "7")           # "37" — both are strings, so + concatenates them
print(3 + 7)               # 10  — both are integers, so + adds them
print("Hello" + " " + "world")  # "Hello world" — concatenation with a space in between
print("5" + 5)             # TypeError — can't use + with a string and an integer

"""## Problem 3

Each `print()` statement below has a bug. Fix all three so they run without errors.

```python
print('It's raining today')
print("She said "good morning"")
print("The answer is: " + 42)
```
"""

print('It's raining today')
print("She said "good morning"")
print("The answer is: " + 42)

"""### Solution"""

print("It's raining today")       # Use double quotes when the text contains an apostrophe
print('She said "good morning"')  # Use single quotes when the text contains double quotes
print("The answer is: " + "42")   # 42 must be a string to concatenate — write it as "42"