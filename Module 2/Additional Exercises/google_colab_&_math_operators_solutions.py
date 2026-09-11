Google Colab & Math Operators - Solutions

## Problem 1

You're shopping for a birthday party. You buy 3 packs of balloons at \$4 each, 2 birthday cakes at \$12 each, and a pack of streamers for \$6. You have a \$5 coupon.

In a single code cell, use `print()` to display:
- The total cost before the coupon
- The total cost after applying the coupon
- The cost per guest if 8 people are attending

**Sample output**
```
42
37
4.625
```
"""

# TODO: calculate and print the total cost before the coupon,
# after the coupon, and cost per guest

"""### Solution"""

# total cost before coupon
print(3 * 4 + 2 * 12 + 6)

# total cost after $5 coupon
print(3 * 4 + 2 * 12 + 6 - 5)

# cost per guest (8 people)
print((3 * 4 + 2 * 12 + 6 - 5) / 8)

"""## Problem 2

You're hanging a square photo backdrop at the party. Each side measures 7 feet. Calculate the area of the backdrop in square feet.

Add a comment above your calculation describing what it does.

**Sample output**
```
49
```
"""

# TODO: calculate and print the area of the backdrop.
# add a comment above your calculation.

"""### Solution"""

# area of 7ft backdrop
print(7 ** 2)

"""## Problem 3

You baked 50 cupcakes for the party and want to pack them into boxes that each hold 6.

- Add a text cell above your code with the heading **Packing Cupcakes**
- In the code cell below, print how many full boxes you can fill and how many cupcakes are left over

**Sample output**
```
8
2
```
"""

# TODO: print the number of full boxes and leftover cupcakes

"""### Solution

Text cell to add above the code:

# Packing Cupcakes
"""

# full boxes
print(50 // 6)

# leftover cupcakes
print(50 % 6)