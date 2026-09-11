#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(a, b):
    return a + b

result = add(5, 10)
print(result)
print(add(result, 20))


# In[3]:


def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
print(greet("Bob"))


# In[4]:


def compute(a, b):
    result = a * b
    if result > 10:
        return result - 3
    else:
        return result + 4

print(compute(3, 2))
print(compute(5, 3))


# In[5]:


counter = 10

def increment(value):
    global counter
    counter += value
    return counter

print(increment(5))
print(increment(3))
print(counter)


# In[ ]:




