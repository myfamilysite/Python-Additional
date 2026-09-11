Watch the solutions video: https://www.youtube.com/watch?v=hFIo05dSD0U&t=8s

This notebook contains 4 practice problems to help you understand how Python functions work.

For each problem, **predict what the code will output before running it**. After you've made your guess, run the cell to check your answer!

### Problem 1
What will be the output of the following code?

def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
print(greet("Bob"))

### Problem 2
Predict the output of this code:

def add(a, b):
    return a + b

result = add(5, 10)
print(result)
print(add(result, 20))

### Problem 3
What will this code print?

def compute(a, b):
    result = a * b
    if result > 10:
        return result - 3
    else:
        return result + 4

print(compute(3, 2))
print(compute(5, 3))

### Problem 4
This function uses a global variable. Can you predict the output?

counter = 10

def increment(value):
    global counter
    counter += value
    return counter

print(increment(5))
print(increment(3))
print(counter)