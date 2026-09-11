square = lambda x: x**2
print(square(5))


# In[7]:


multiply = lambda x,y: x*y
print(multiply(3, 7))


# In[8]:


nums = [1, 2, 3, 4, 5]
doubled = map(lambda x: x*2, nums)
print(list(doubled))


# In[13]:


words = ['hi', 'hello', 'sun', 'amazing', 'cat']
long_words = filter(lambda x:len(x)>4, words)
print(list(long_words))


# In[15]:


students = [('Alice', 88), ('Bob', 72), ('Charlie', 95)]
sorted_students = sorted(students, key=lambda x:x[1])
print(sorted_students)




