#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = "Soumya"
print(name.upper())


# In[2]:


x = "nOtEbOOK"
print(x.casefold())


# In[3]:


x = "BANANA"
print(x.islower())


# In[5]:


y = "oranges"
print(y.center(100))


# In[6]:


x = "Hello Rahul"
y = x.replace("Rahul","Soumya")
print(y)


# In[7]:


txt = "can you can a can like a canner can can a can?"
print(txt.count("can"))


# In[9]:


txt_2 = "How are you doing?"
print(txt_2.find("you"))


# In[11]:


txt_3 = "            hello            "
x = txt_3.lstrip()
print(x)


# In[12]:


txt = "This is not an encoded message"
x = txt.encode(encoding = "ASCII", errors = "ignore")
print(x)


# In[13]:


txt = "I don't like oranges or apples!"
x = txt.partition("like")
print(x)


# In[15]:


x = 90.1412
print(int(x))


# In[16]:


x = 9
print(float(x))


# In[17]:


x = [10,13,15,19]
print(tuple(x))


# In[18]:


x = 35
print(complex(x))


# In[20]:


x = "False"
print(bool(x))


# In[23]:


a = 1
b = 5
print("a is greater") if a > b else print("a is not greater")


# In[26]:


a = 10
b = 54
if a <= b: print("a is smaller than b")


# In[ ]:




