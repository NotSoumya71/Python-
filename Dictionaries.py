#!/usr/bin/env python
# coding: utf-8

# In[1]:


dict1 = {
           "Apple" : "A seasonal red fruit",
           "Can" : "A container",
           "Nest" : "A bird's home"
}

print(dict1)


# In[2]:


print(dict1["Can"])

# dictionaries are ordered so you can get a value from the key.


# In[3]:


dict1["Can"] = "A container used to store something"
print(dict1)

# we can add, modify, and change any item in a dictionary.


# In[5]:


student = {
            "Name" : "Soumya Singh",
            "Class" : 8,
            "Age" : 12.75,
            "Gender" : "Female",
            "isAdult" : False
}
print(student)

# dictionaries allow multiple data types at the same time.


# In[8]:


x = {
      "First Name" : "Sakshi",
      "Last Name" : "Singh",
      "Age" : 19,
      "Age" : 20,
      "Age" : 21
}

print(x)

# dictionaries overwrite the duplicate value with the most recent value entered.


# In[9]:


print(type(x))


# In[10]:


print(len(x))


# In[11]:


print(len(student))


# In[12]:


y = dict(name = "Soumya", age = 22, State = "Maharashtra", wannabe = True)
print(y)

# a dictionary constructor


# In[13]:


for i in student:
    print(i)


# In[18]:


z = y.get("name")
print(z)

# we can acces any item of a dictionary using the get function


# In[19]:


z = y.keys()
print(z)

# returns a list of all keys of dictionary


# In[20]:


z = y.values()
print(z)
# returns the value of all keys


# In[21]:


z = y.items()
print(z)

# returns the pair of key and values together


# In[23]:


if "age" in y:
    print("yes")
else:
    print("No")
    
# we can use the membership operator in to check whether a key is present or not


# In[ ]:




