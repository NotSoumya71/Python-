#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers = [3,5,6,8,9,10]
squares = []
for i in numbers:
    x = i*i
    squares.append(x)
print(squares)


# In[5]:


def number(list1):
    x = list1[0]
    for i in list1:
        if i != x:
            print("All the items are not same")
            break
    else:
        print("All items are the same")
        
li = [1,1,1,1,1,1]
li2 = [1,1,1,1,3,2,1]
number(li)
number(li2)


# In[6]:


def check_tuple(tup):
    x = tup[0]
    for i in tup:
        if i != x:
            print("All items are not the same")
            break
    else:
        print("All items are the same")
tup = (1,1,1,1,1,1)
tup2 = (1,2,3,4,1,1)
check_tuple(tup)
check_tuple(tup2)


# In[8]:


tupl = (12,43,65,23,87)
tup2 = tupl[::-1]
print(tup2)


# In[10]:


tupl = (12,43,65,23,87)
sum = 0
for i in tupl:
    sum = sum + i
print("The sum is,", sum)


# In[11]:


tuple1 = (1,2,3,4,5)
list1 = [6,7,8,9,10]
list2 = list1.copy()

li = list(tuple1)
li.extend(list2)
new_tuple = tuple(li)

list1.extend(tuple1)

print(new_tuple)
print(list1)


# In[12]:


tuple_1 = (3,24)
dec = tuple_1[1]
dec /= 100
whole = tuple_1[0]

number = whole + dec
print(number)


# In[ ]:




