#!/usr/bin/env python
# coding: utf-8

# In[3]:


x = {"Apple","Banana","Cherry"}
print(x)
print(type(x))

#sets use curly braces


# In[4]:


y = {12,1.342,True,"Python"}
print(y)

#sets have different data types.


# In[5]:


set1 = {"Laptop","Mobile","iPad","Smartwatch","Earphones"}
set1[0] = "PC"
print(set1)

#sets are unchangeable, we cannot update the value of a set.

#Note:- We can add or remove items in a set, but cannot change existing values.


# In[6]:


set2 = {"Tiger","Lion","Elephant","Giraffe","Deer"}
print(set2[0:4])

#sets are unordered and unindexed.


# In[9]:


duplicate = {"toy","clothes","bags","toy","guitar"}
print(duplicate)

#sets do not allow duplicates


# In[10]:


set3 = {"Apple","Guava",True,1,2}
print(set3)

#True and 1 is considered to be the same item, as 1 is considered to be a boolean value.

set4 = {0,3,2,False}
print(set4)

#False and 0 is considered to be the same value too, as 0 is also considered to be a boolean value.


# In[11]:


set1 = {1,2,3,4,5,6,2,7,8,2,9,10}
print(len(set1))


# In[12]:


set_1 = set(("Apple","Samsung","Xiaomi","Realme","Oppo","Motorola","Huawei"))
print(set_1)
print(type(set_1))

#set constructor can also be used to make a set.


# In[ ]:




