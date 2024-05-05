#!/usr/bin/env python
# coding: utf-8

# In[2]:


class_7C = ["Soumya", "Devansh", "Lavanya", "Mayank", "Advika", "Siddharth"]
for x in class_7C:
    print(x)
    if x == "Lavanya":
        break
#break is used to stop the iteration


# In[21]:


list1 = ["apple", "orange", "grape", "banana", "watermelon", "pineapple"]
for x in list1:
    if x == "banana":
        continue
    print(x)
#continue statement stops the current iteration of the loop and continues with the next one.


# In[5]:


for x in range(9):
    print(x)
#the range function has a default starting value of  0.


# In[13]:


for x in range(6):
    print(x)
    if x ==2: break
else:
    print("Finished!")
#every time we use a break statement, else does not get executed.


# In[22]:


for x in [0,1,2]:
    pass
#pass statement is used to avoid unwanted errors or simply to pass a statement


# In[25]:


#nested for loops 
colours = ["red", "yellow", "green"]
fruits = ["apple","banana","kiwi"]
for x in colours:
    for y in fruits:
        print(x,y)


# In[1]:


#More examples:
sandwich = ["tomato", "cucumber", "ketchup","cheese", "bread"]
for x in sandwich:
    if x == "ketchup":
        continue
    print(x)


# In[2]:


tuple_1 = ("science","math","english","history","geography")
s = input("Subject:")
for x in tuple_1:
    print(x)
    if x == s:
        break


# In[3]:


key = {
        "name" : "siddharth",
        "age"  : 13,
        "gender" : "male"
}
for x in key:
    print(x)
#note:- only prints the key of a dictionary...


# In[4]:


items = {"Bag","shoes","umbrella"}
colour = ["blue","orange","green"]
for x in items:
    for y in colour:
        print(y,x)


# In[ ]:




