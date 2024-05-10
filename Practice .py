#!/usr/bin/env python
# coding: utf-8

# In[1]:


#factorial of a number
num = int(input())
factorial = 1
if num < 0:
    print("Cannot find factorial of a negative number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("Factorial of",num,"is",factorial)


# In[4]:


#reversing a number
num = int(input())
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("reversed number of",temp,"is",rev)


# In[5]:


#checking if a number is a palindrome
num = int(input())
temp = num
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if rev == temp:
    print("Number is palindrome!")
else:
    print("Number is not a palindrome!")


# In[6]:


#checking if a string is a palindrome (reversing a string)
string = input()
string_reverse = (string[:: -1])
print("Reversed string:",string_reverse)
if string_reverse == string:
    print(string,"is a palindrome!")
else:
    print(string,"is not a palindrome!")


# In[7]:


#checking if a number is an armstrong number
num = int(input())
sum = 0
temp = num
while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num //= 10
if sum == temp:
    print(temp,"is an Armstrong number!")
else:
    print(temp,"is not an Armstrong number!")


# In[9]:


#fibonacci series
first = 0
second = 1
print(first)
print(second)
third = first+second
while third < 100:
    print(third)
    first = second
    second = third
    third = first+second


# In[16]:


colours = ["blue","red","yellow","white"]
flowers = ["orchid","roses","sunflowers","tulips"]
for x in flowers:
    for y in colours:
        print(y,x)
        if x == "sunflowers":
            continue


# In[4]:


num_1 = int(input("Enter the first number"))
num_2 = int(input("Enter the second number"))
op = input("Enter the operator:")
if op == "+":
    print(num_1+num_2)
elif op == "-":
    print(num_1-num_2)
elif op == "*" or op == "x":
    print(num_1*num_2)
elif op == "/":
    print(num_1/num_2)
elif op == "//":
    print(num_1//num_2)
elif op == "%":
    print(num_1%num_2)
else:
    print("Please choose a valid operator")


# In[11]:


num = int(input())
is_prime = True
i = 2
while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i +=1
if is_prime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# In[19]:


sum = 0
i = 1
while i <= 100:
    sum = sum + i
    i +=1
print(sum)


# In[20]:


sum = 0
i = 1
while i <= 10:
    sum = sum + i**2
    i +=1
print(sum)


# In[ ]:




