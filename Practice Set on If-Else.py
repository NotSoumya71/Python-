#!/usr/bin/env python
# coding: utf-8

# In[1]:


t = int(input("Enter temperature"))
q = input("Enter unit")
if q == "C":
    print(t*9/5+32,"F")
elif q == "F":
    print((t - 32) * 5/9,"C")
else:
    print("Wrong unit")


# In[2]:


num_1 = int(input())
num_2 = int(input())
if num_1 == num_2:
    print("They are equal")
elif num_1 > num_2:
    print(num_1, "is greater than", num_2)
else:
    print(num_1, "is smaller than", num_2)


# In[3]:


height = float(input("Height in Meters:"))
weight = float(input("Weight in Kilograms:"))
bmi = weight / (height*height)
if bmi < 18.5:
    print("Your bmi is", bmi,". It falls within the underweight range")
elif bmi >= 18.5 and bmi < 25:
    print("Your bmi is", bmi,". It falls within the healthy weight range")
elif bmi >= 25 and bmi < 30:
        print("Your bmi is", bmi,". It falls within the overweight range")
else:
        print("Your bmi is", bmi,". It falls within the obesity range")


# In[5]:


age = int(input("Enter age"))
if age <= 12:
    print("Child")
elif age > 12 and age < 21:
    print("Teenager")
elif age >= 21 and age < 60:
    print("Adult")
else:
    print("Senior")


# In[7]:


year = int(input("Enter year"))
if year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")


# In[9]:


s = float(input())
if s > 60:
    print("Pass,")
    if s >= 90:
        print("grade A!")
    elif s >= 80 and s < 90:
        print("grade B!")
    elif s >= 70 and s < 80:
        print("grade C!")
    else:
        print("grade D!")
else:
    print("Fail, grade F!")


# In[10]:


age = int(input("Enter age of customer"))
time = int(input("Enter time in hours"))
if age < 12:
    if time < 1700:
        print("Ticket price is $5")
    else:
        print("Ticket price is $7")
elif age >= 12 and age < 60:
    if time < 1700:
        print("Ticket price is $10")
    else:
        print("Ticket price is $12")
else:
    if time < 1700:
        print("Ticket price is $7")
    else:
        print("Ticket price is $9")


# In[11]:


vote = int(input("Enter Age:"))
if vote < 18:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")


# In[14]:


vowel = ("a", "e", "i", "o", "u")
vowel_caps = ("A","E","I","O","U")
lett = input("Enter Letter")
if lett in vowel:
    print(lett, "is a vowel")
else:
    if lett in vowel_caps:
        print(lett, "is a vowel")
    else:
        print(lett, "is not a vowel")


# In[ ]:




