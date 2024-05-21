#!/usr/bin/env python
# coding: utf-8

# In[2]:


#id is a pre-defined function which returns the actual location of the object.
a = "MyName"
b = "MyName"
print(id(a))
print(id(b))
print(a is b)


# In[3]:


a = [20,30,40]
b = [20,30,40]
print(id(a))
print(id(b))
print(a is b)


# In[4]:


x = "old value"
def immutable(x):
    x = "new value"
    print("Inside function:",x)
print("Outside function:",x)
immutable(x)


# In[5]:


def mutable(a):
    a[0] = "Sakshi"
    print("Inside function",a)
bar = ["Name","How","are","you","doing?"]
mutable(bar)
print("Outside function:",bar)


# In[6]:


#example of calling a function inside another function.

def SquareOf(x):
    return(x*x)
def SumOfSquares(Array,n):
    
    sum = 0
    for i in range(n):
        SquaredValue = SquareOf(Array[i])
        
        sum += SquaredValue
    return sum

Array = [1,2,3,4,5,6,7,8,9,10]

n = len(Array)

Total = SumOfSquares(Array,n)

print("The sum is:", Total)


# In[ ]:




