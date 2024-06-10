#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to accessing items one by one in a set, we can use a for loop.
x = {"Car","Bus","Truck","Bike","Motorcycle","Race Car"}
for i in x:
    print(i)
#note:- A set is unordered!


# In[2]:


#we can check if a particular item is present in a set through membership operators.
print("Car" in x)


# In[3]:


print("Hut" in x)


# In[4]:


print("Bus" not in x)


# In[5]:


#we cannot modify an existing item in a set, but,
#We can remove an existing item, and add a new item.

y = {10,20,30,40,50}
y.remove(20)
print(y)


# In[6]:


y.add(22)
print(y)


# In[8]:


#update() is used to add a set to another set. It can also be used to add another iterable.
set1 = {"Piano","Guitar","Kalimba","Harp","Sitar","Tabla"}
set2 = {"Drums","Bass","Violin","Oboe","Flute","Sarod"}
set1.update(set2)
print(set1)


# In[9]:


tup = ("Amplifier","Tuner","Headphones","Speakers")
set2.update(tup)
print(set2)


# In[12]:


#another way of removing an item.
set2.discard("Bass")
print(set2)


# In[13]:


#randomly removes an item
set_1 = {1,2,3,4,5}
set_1.pop()
print(set_1)


# In[15]:


#empties out the set
set_1.clear()
print(set_1)


# In[16]:


#the difference between discard and remove is this:
set5 = {"a","b","c","d","e"}
set5.remove("f")
print(set5)


# In[18]:


set5.discard("f")
print(set5)
#the above lines of code show that remove displays error when a non-existing item is put as the arguement.
#on the other hand, discard does not show any error for the same.


# In[ ]:




