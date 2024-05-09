#!/usr/bin/env python
# coding: utf-8

# In[1]:


#armstrong numbers
num = int(input())
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num //= 10
if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# In[2]:


#factorial
num = int(input())
factorial = 1
if num < 0:
    print("Negative numbers don't have a factorial!")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("Factorial of",num,"is",factorial)


# In[3]:


num = int(input())
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number is",rev)


# In[4]:


num=int(input())
num_2 = num*1
r = 0
while num != 0:
    digit = num % 10
    r = r * 10 + digit
    num = num // 10
if r == num_2:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")


# In[5]:


string = input()
if (string == string[:: -1]):
    print(string,"is palindrome")
else:
    print(string,"is not palindrome")
    


# In[ ]:




