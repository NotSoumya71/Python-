#!/usr/bin/env python
# coding: utf-8

# In[1]:


set1 = {11,12,13,14,15}
set2 = {11,13,15,17,19,21}
diff = set1.difference(set2)
dif = set2.difference(set1)
print(diff)
print(dif)


# In[2]:


lst = ["Guitar","Keyboard","Kalimba","Drums","Keyboard","Drums","Clarinet","Sitar","Guitar"]
set1 = set(lst)
print(set1)


# In[4]:


list1 = [12,1,14,64,4,67,3,90,52,41,7,0]
list1.sort(reverse = True)
n1 = list1[0]
n2 = list1[1]
print("The numbers with the largest product are:",n1,"and",n2)


# In[7]:


set1 = {13,14,15,43,76,643}
set2 = {154,25,75,25,855,36,35}
n1 = int(input())
n2 = int(input())
if n1 in set2 or n2 in set2:
    print("Number exists in set")
else:
    set1.add(n1)
    set1.add(n2)
    print(set1)


# In[8]:


set_a = {"Dates","Raisins","Cashew"}
set_b = {"Walnut","Pistachio","Cashew","Dates"}
diff = set_b.difference(set_a)
set_a.update(diff)
print(set_a)


# In[13]:


ls1 = [17,3,6,4,9,1,2,86,5,0,54,12]
pairs = set(())
value = int(input("Enter the sum: "))
for num in ls1:
    num2 = value - num
    if num2 in ls1:
        pairs.add(num)
        pairs.add(num2)
print(pairs)


# In[16]:


strings = ["this","is","a","list","and","this","list","has","strings","!"]
unique = set(())
repeated = set(())
for i in strings:
    countt = strings.count(i)
    if countt == 1:
        unique.add(i)
    else:
        repeated.add(i)
print("Unique words: ",unique)
print("Repeated words: ",repeated)
for x in repeated:
    c = strings.count(x)
    print(x,"appeared",c,"times")


# In[19]:


set2 = {12,45,32,4,1,0,54,74,13,43,39}
list1 = list(set2)
largest = list1[0]
for x in list1:
    if x > largest:
        largest = x
print("Largest item in",set2,"is",largest)

smallest = list1[0]
for i in list1:
    if i < smallest:
        smallest = i
print("Smallest item in",set2,"is",smallest)


# In[ ]:




