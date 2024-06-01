#!/usr/bin/env python
# coding: utf-8

# In[1]:


tup = (10,20,30,40,50)
print(tup)


# In[2]:


print(tup[1])


# In[3]:


print(tup[1:4])


# In[4]:


tup = ("Soumya",12,True,3.14,9403,False)
print(tup)


# In[5]:


tup2 = ("Apple","Orange","Banana","Cherries","Papaya","Watermelon")
print(len(tup2))


# In[7]:


tup1 = (1,2,3,4,5,6,7,8,9)
print(tup1[-7:-2])


# In[8]:


tup3 = (10,11,12,13,21,14,15)
li = list(tup3)
li.remove(21)
tup3 = tuple(li)
print(tup3)


# In[9]:


x = ("A","E","I","O")
y = list(x)
y.append("U")
x = tuple(y)
print(x)


# In[10]:


tupl = (123,1643,256,3,43)
lst = list(tupl)
lst[3] = 354
tupl = tuple(lst)
print(tupl)


# In[11]:


t1 = (10,20,30,40,50)
t2 = (60,70,80,90,100)
t1 = t1 + t2
print(t1)


# In[12]:


ot = ("Sugar","Wheat","Milk","Fruits")
del ot
print(ot)


# In[13]:


x = ("Soumya",)
print(x)
print(type(x))


# In[20]:


z = tuple((10,11,12,13,14))
print(z)
print(type(z))


# In[22]:


x = (14,15,34,246,353,245,32)
i = 0
while i < len(x):
    print(x[i])
    i = i+1


# In[24]:


x = ("Apple","Banana","Dragonfruit")
(red,yellow,white) = x
print(red)
print(yellow)
print(white)


# In[25]:


x1 = (12,25,56,41,42)
x2 = (15,70,96,60,24)
x3 = x1 + x2
print(x3)


# In[26]:


tup = (20,30,40,50)
tup2 = tup * 3
print(tup2)


# In[27]:


tup1 = (1,1,1,1,1,1,5,4,3,2,5,6,4,2,7,9,9,7,7,7,9,8,8,8,6,6,1,1,1,35,342,1,3)
x = tup1.count(1)
print(x)
#count function determines the count of an item, how many times it has appered in a tuple.


# In[30]:


tup2 = (10,12,14,16,18,20,22)
x = tup2.index(10)
print(x)
#returns the index of an item.


# In[33]:


tup3 = ("Apple","Cherry","Beetroot","Banana","Papaya")
(*red,yellow,orange) = tup3
print(red)
print(yellow)
print(orange)


# In[ ]:




