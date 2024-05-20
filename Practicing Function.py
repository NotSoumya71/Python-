#!/usr/bin/env python
# coding: utf-8

# In[3]:


def factorial(num_1):
    factorial = 1
    for i in range(1,num_1+1):
        factorial*=i
    print("Factorial of",num_1,"is",factorial)

factorial(6)


# In[7]:


def palindrome(num):
    rev = 0
    temp = num
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    print("Reversed is",rev)
    if rev == temp:
        print("Number is palindrome!")
    else:
        print("Number is not palindrome!")
        
palindrome(123321)


# In[12]:


def country(country="India"):
    print("I am from",country)
country("Brazil")
country()
country("Pakistan")


# In[10]:


def pass_statment(num_1):
    pass


# In[11]:


def myfun(x):
    return x / 10
print(myfun(30))
print(myfun(45))
print(myfun(87))


# In[14]:


def my_fun(fname):
    print("Hello",fname+"!")
    
my_fun("Soumya")


# In[16]:


#Calling a function by its value:
string = "Soumya"
def name(string):
    string = "Sakshi"
    print("Inside function:",string)
name(string)
print("Outside function:",string)


# In[17]:


#Calling a function by its reference:
def add_item(list):
    list.append(50)
    print("Inside function:",list)
#(append is used to add an item to the list)

mylist = [10,20,30,40]

add_item(mylist)
print("Outside function:",mylist)


# In[ ]:




