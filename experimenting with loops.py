#!/usr/bin/env python
# coding: utf-8

# In[5]:


#factorial of a number
f = int(input())
factorial = 1
if f < 0:
    print("cannot find factorial for negative numbers")
elif f == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,f+1):
        factorial = factorial * i
    print("the factorial of",f,"is",factorial)


# In[9]:


#reversing a number
num = int(input())
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number is",rev)


# In[16]:


#checking if a number is a palindrome
num = int(input())
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if (num == reverse):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")


# In[ ]:




