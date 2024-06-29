#!/usr/bin/env python
# coding: utf-8

# In[1]:


# tuples 

tup1 = ("Apple","Banana","Orange")
print(tup1)

# tuples use round brackets


# In[2]:


list1 = list(tup1)
list1.append("Mango")
tup1 = tuple(list1)
print(tup1)
print(type(tup1))

# tuples are unchangeable 


# In[4]:


list1 = list(tup1)
list1.remove("Orange")
tup1 = tuple(list1)
print(tup1)


# In[5]:


for x in tup1:
    print(x)
    if x == "Banana":
        break
# looping through a tuple


# In[7]:


print(tup1[0])

# tuples are ordered


# In[8]:


tup2 = (15,16,17,19,16,20,21)
print(tup2)
# tupels allow duplicates


# In[9]:


tup2 = (False,10,"String",10+3j,True,20.435)
print(tup2)
# tuples support different data types 


# In[10]:


# lists

li1 = [10,20,30,40,50,60]
for x in li1:
    print(x);


# In[11]:


li1[2] = 25
print(li1)

# lists are ordered


# In[14]:


li1.remove(10)
print(li1)

# lists are changeable


# In[15]:


li1.pop()
print(li1)


# In[16]:


li1.extend(tup1)
print(li1)

# adding tuple to list


# In[17]:


li2 = [30,True,9+1j,"List",10.4357,"string"]
print(li2)

# lists support different data types


# In[19]:


li2.append("List")
print(li2)

# lists support duplicates


# In[20]:


i = 0
while i < len(li1):
    print(li1[i])
    i+=1


# In[21]:


# sets

set1 = {12,14,16,18,20,22,24,26}
print(set1)

# sets are unordered and unindexed


# In[22]:


set1.add(28)
print(set1)

# sets are changeable


# In[23]:


set1.pop()
print(set1)

# removes an item


# In[26]:


set2 = {12,12,14,16,18,20,12,15}
print(set2)

# sets do not allow duplicates


# In[28]:


set2.add("String")
print(set2)
 
# sets allow different data types at once


# In[30]:


set3 = set(("this","is","a","set"))
print(set3)

# set constructor


# In[33]:


for x in set1:
    if x == 20:
        continue
    print(x)


# In[34]:


# dictionaries

dict1 = {
        "Name" : "Soumya",
        "Age" : 12,
        "Nationality" : "Indian",
        "isAdult" : False
}

print(dict1)


# In[36]:


for x in dict1:
    print(x)


# In[37]:


for x in dict1.items():
    print(x)


# In[38]:


for x in dict1.values():
    print(x)


# In[42]:


dict1["Age"] = 13
print(dict1)


# In[48]:


dict1.pop("Age")
print(dict1)


# In[50]:


setx = {12,13,14,15,16}
sety = {17,8,19,14,12}
setx.symmetric_difference_update(sety)
print(setx)


# In[51]:


set1 = {10,20,30,40}
set2 = {10,15,20,15,30,35,5}
i = set1.intersection(set2)
print(i)


# In[53]:


tup1 = ("Apple","Banana","Pineapple")
(red,*yellow) = tup1
print(yellow)
print(red)


# In[55]:


dict1.update({"Birthday":"15th September"})
print(dict1)


# In[58]:


dict1["City"] = "Nagpur"
print(dict1)


# In[60]:


family = {
    "Father" : {
        "Name" : "Hemant",
        "Profession": "Engineer",
        "Age" : 49
    },
    "Mother" : {
        "Name" : "Smita\n",
        "Profession": "Engineer\n",
        "Age": 46
    },
    "Sister" : {
        "Name" : "Sakshi\n",
        "Profession": "Student/Intern\n",
        "Age": 21
    },
    "Me" : {
        "Name" : "Soumya",
        "Profession": "Student",
        "Age" : 13
    }
}
print(family)


# In[ ]:




