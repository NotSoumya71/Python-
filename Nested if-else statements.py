#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nested if else statements
x = 15

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and above 20!")
    else:
        print("Not above 20")
else:
    print("Less than 10")


# In[3]:


x = int(input("Enter a number"))
if x > 0:
    if x % 2 == 0:
        print("Even")
    else:
        print("odd")


# In[5]:


x = int(input("Enter a number"))
if x > 0:
    if x % 2 == 0: 
        print("even,")
        if x > 10:
            print("greater than 10,")
            if x > 20:
                print("greater than 20,")
                if x > 35:
                    print("and greater than 35!")
                else: 
                    print("but not greater than 35")
            else:
                print("but not gretaer than 20")
        else:
            print("but not greater than 10")
    else:
        ("Odd.")
else:
    ("Not greater than 0")


# In[ ]:




