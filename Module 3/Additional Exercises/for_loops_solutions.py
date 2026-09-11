# For Loops - Solutions

## Problem 1

A bookstore keeps a list of staff picks for the month:


staff_picks = ["The Alchemist", "Atomic Habits", "Dune", "Sapiens"]

Use a for loop to print each title.

**Sample output**
```
The Alchemist
Atomic Habits
Dune
Sapiens
```
"""

staff_picks = ["The Alchemist", "Atomic Habits", "Dune", "Sapiens"]

# TODO: Loop through staff_picks and print each title

"""### Solution"""

staff_picks = ["The Alchemist", "Atomic Habits", "Dune", "Sapiens"]

for book in staff_picks:
    print(book)

"""## Problem 2

The bookstore is assigning temporary ID numbers to 6 new arrivals, starting from 0.

Use a for loop with `range()` to print each ID number.

**Sample output**
```
Book ID: 0
Book ID: 1
Book ID: 2
Book ID: 3
Book ID: 4
Book ID: 5
```
"""

# TODO: Use range() to print Book ID numbers 0 through 5

"""### Solution"""

for book_id in range(6):
    print(f"Book ID: {book_id}")

# Note for script: range(0, 6) is equivalent — worth mentioning both forms

"""## Problem 3

The bookstore is running a clearance sale and offering a 15% discount on a set of books.

```python
prices = [10.00, 15.00, 20.00, 25.00]
discount = 0.15
```

Use a for loop to print both the original price and the discounted price for each book.

**Sample output**
```
Original: 10.0
Discounted: 8.5
Original: 15.0
Discounted: 12.75
Original: 20.0
Discounted: 17.0
Original: 25.0
Discounted: 21.25
```
"""

prices = [10.00, 15.00, 20.00, 25.00]
discount = 0.15

# TODO: Loop through prices and print both the original and discounted price for each

"""### Solution"""

prices = [10.00, 15.00, 20.00, 25.00]
discount = 0.15

for price in prices:
    print(f"Original: {price}")
    print(f"Discounted: {price * (1 - discount)}")