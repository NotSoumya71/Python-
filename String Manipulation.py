#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = "math"
x = a.capitalize()
print(x)
#capitalize makes the first alphabet captial.


# In[3]:


b = "KeYbOArD"
x = b.casefold()
print(x)
#casefold makes everything lowercase.


# In[4]:


a = "Pineapple"
x = a.center(80)
print(x)
#centers the string, by the value entered as arguement.


# In[6]:


b = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
x = b.count("wood")
print(b)
print(x)
#count is used to count the number of times a word has appeared.


# In[7]:


a = "This is an encoded message"
print(a.encode(encoding="ascii", errors="ignore"))
#encode is used to encode the text into a different form so that it can't be understood by anyone


# In[4]:


b = "She loves to read books."
print(b.endswith("."))
#Endswith helps in finding out the last character of a sentence.


# In[5]:


a = "Peter piper picked a peck of pickled peppers."
print(a.find("peck"))
#Find is used to locate a particular word in a string.


# In[4]:


x = "I like {ffruit}".format(ffruit = "Watermelon")
print(x)
#format helps in formatting specified values.


# In[6]:


x = "notebook"
a = x.islower()
print(a)
#checks if the mentioned string is in lowercase or not.


# In[8]:


a = "GUItaR
x = a.isupper()
print(x)
b = "GUITAR"
x = b.isupper()
print(x)
#checks is the mentioned string is in uppercase or not.


# In[11]:


a = "hello//,, \n How are you *65143^%3?"
x = a.isprintable()
print(x)
#checks if the entered string is printable or not.


# In[14]:


x = "9248394"
print(x.isdigit())
#checks if the entered string is a digit


# In[15]:


a = "Hello, how are you?"
x = a.split(",")
print(x)
#splits the string at the mentioned point


# In[17]:


txt = "          fruits            "
x = txt.lstrip()
print("I like to eat", x, "everyday")
#gives you a left trim version of a string.


# In[21]:


txt = "An apple a day keeps the doctor away."
x = txt.partition("day")
print(x)
#partiton returns a tuple, where the string is splitted.


# In[22]:


txt = "SoUmYA"
x = txt.swapcase()
print(x)
#swapcase swaps the cases of alphabets


# In[23]:


a = "glass"
x = a.upper()
print(x)
#converts everything to uppercase.


# In[25]:


a = "I do not like oranges anymore."
x = a.startswith("I")
print(x)


# In[1]:


am= "I like oranges"
x = am.replace("oranges", "bananas")
print(x)


# In[ ]:




