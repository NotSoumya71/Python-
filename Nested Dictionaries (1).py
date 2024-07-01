#!/usr/bin/env python
# coding: utf-8

# In[1]:


teachers = {
    "teacher1" : {
        "Name" : "Sameer",
        "Subject" : "Social Science"
    },
    "teacher2" : {
        "Name" : "Sunita P.",
        "Subject" : "Hindi"
    },
    "teacher3" : {
        "Name" : "Anuradha",
        "Subject" : "Math"
    }
}

print(teachers)


# In[3]:


city1 = {
    "Name" : "Mumbai",
    "State" : "Maharashtra",
    "Country" : "India"
}

city2 = {
    "Name" : "Lucknow",
    "State" : "Uttar Pradesh",
    "Country" : "India"
}

city3 = {
    "Name" : "Hyderabad",
    "State" : "Telangana",
    "Country" : "India"
}

cities = {
    "city1" : city1,
    "city2" : city2,
    "city3" : city3
}
print(cities)


# In[4]:


print(city1["Name"])


# In[6]:


print(cities["city2"]["Name"])


# In[11]:


for x,o in cities.items():
    print(x)
    for y in o:
        print(y + ":", o[y])


# In[16]:


phone = {
    "brand" : "Apple",
    "Storage" : "64 GB",
    "Model" : 12
}
x = phone.setdefault("Colour", "Lavender")
print(phone)

# used to add another key to a dictionary


# In[ ]:




