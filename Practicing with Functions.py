#!/usr/bin/env python
# coding: utf-8

# In[7]:


def my_calculator(num_1,num_2): 
    operator = input("Enter an operator:")
    if operator == "+":
        print(num_1+num_2)
    elif operator == "-":
        print(num_1 - num_2)
    elif operator == "*":
        print(num_1*num_2)
    elif operator == "/":
        print(num_1/num_2)
    elif operator == "//":
        print(num_1//num_2)
    elif operator == "%":
        print(num_1%num_2)
    else:
        print("Please enter a valid operator")
        
my_calculator(20,5)


# In[8]:


def function_1(num_1,num_2):
    print(num_1+num_2)
function_1(5,20)


# In[4]:


def fun_2(num_1,num_2):
    print(num_1+num_2)
    print(num_1-num_2)
    print(num_1*num_2)

fun_2(20,10)


# In[10]:


def factorial(num):
    factorial = 1
    if num < 0:
        print("Cannot find factorial for negative numbers")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        print("Factorial of",num,"is",factorial)
        
factorial(5)


# In[11]:


def armstrong(num):
    sum = 0
    temp = num
    while num > 0:
        digit = num % 10
        sum = sum + digit**3
        num //= 10
    if sum == temp:
        print(temp,"is an Armstrong number")

armstrong(407)


# In[12]:


def palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num%10
        rev = rev*10+digit
        num //= 10
    if temp == rev:
        print(temp,"is a palindrome")
    else:
        print(temp,"is not a palindrome")

palindrome(123321)
palindrome(123421)


# In[16]:


def square(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit**2
        num //= 10
    print(sum)

square(25)
square(154)


# In[17]:


def largest_number(num_1,num_2,num_3):
    if num_1 > num_2 and num_1 > num_3:
        print(num_1,"is the largest number")
    elif num_2 > num_1 and num_2 > num_3:
        print(num_2,"is the largest number")
    else:
        print(num_3,"is the largest number")

largest_number(2,5,3)


# In[ ]:




