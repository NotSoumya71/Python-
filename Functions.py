#!/usr/bin/env python
# coding: utf-8

# In[2]:


def my_fun1(fname, lname):
    print(fname + " " + lname)
my_fun1("Soumya","Singh")


# In[4]:


#*args is used when we don't know the number of arguements that are going to be there. It is also called arbitrary arguement
def my_function(*kids):
    print("The youngest child is" + " " + kids[2])
    
my_function("Radhika","Abhijeet","Anand","Aparna")


# In[6]:


def myfun_2(child1, child2, child3, child4):
    print("The youngest child is",child3)
myfun_2(child1 = "Radhika",child2 = "Sejal", child3 = "Devansh", child4 = "Vedanshi")


# In[8]:


#**kwargs is used when we do not know the number of keyword arguments.
def myfun_3(**kid):
    print("last name is" + " " + kid["lname"])
myfun_3(fname = "Sakshi", lname = "Singh")


# In[10]:


def country_name(country = "India"):
    print("I am from " + country)
country_name("Brazil")
country_name("Fance")
country_name()
country_name("Japan")
#default value is used when the user does not specify a value


# In[11]:


def myfun_5(x):
    return x / 10
print(myfun_5(30))
print(myfun_5(45))
print(myfun_5(87))
# a function always returns a value from the function, you have to print it later to get the result


# In[13]:


def my_fun():
    pass


# In[15]:


def function_1(subject = "Math"):
    print("I studied " + subject)
function_1("Science")
function_1()
function_1("Sanskrit")


# In[16]:


def function(x, y):
    return x * y
print(function(10, 2))
print(function(22, 8))


# In[ ]:




