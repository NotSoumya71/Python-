#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruit = input("What is your favourite fruit?")
print("You like", fruit)


# In[4]:


a = int(input("Enter a number"))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")


# In[7]:


a = int(input("Enter a number"))
b = int(input("Enter a number"))
if a > b:
    print(a, "is greater than", b)
elif a==b:
     print(a, "is equal to", b)
else:
    print(a, "is smaller than", b)


# In[8]:


a = 7604
b = 5039
if a > b: print(a, "is greater than", b)


# In[10]:


a = 3139
b = 5039
print(a, "is greater than", b) if a > b else print(a, "is not greater than", b)


# In[11]:


a = 10
b = 302
c = 9
if a > c and b > c:
    print("c is the smallest one")
elif a > b and c > b:
    print("b is the smallest one")
else:
    print("a is the smallest one")


# In[14]:


a = 10
b = 19
c = 24
if a > c or b > c:
    print("1")
else:
    print("2")


# In[15]:


a = 10
b = 5
if not a > b:
    print("a is smaller than b")
else: 
    print("a is greater than b")

