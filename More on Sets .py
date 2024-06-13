#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = {10,20,30,40,50}
y = {"a","b","c","d","e"}
z = x.union(y)
print(z)
# joins two sets together


# In[2]:


x = {10,20,30,40}
y = {"a","b","c","d"}
z1 = x | y
print(z1)
# | operator can be used for union


# In[3]:


set1 = {1,2,3,4,5}
set2 = {10,20,30,40,50}
set3 = {"A","B","C","D","E"}
set4 = {"v","w","x","y","z"}
union = set1 | set2 | set3 | set4
print(union)

# multiple sets joined together


# In[5]:


list1 = ["this","is","a","list"]
set1 = {"v","w","x","y","z"}
uni = set1.union(list1)
print(uni)

# union can also be used to join any other iterable


# In[6]:


set1 = {1,2,3,4,5,6}
set2 = {0,2,4,6,8}
inter = set1.intersection(set2)
print(inter)

#prints the common elements of two sets


# In[7]:


set1 = {1,2,3,4,5,6}
set2 = {0,2,4,6,8}
inter = set1 & set2
print(inter)

# & can be used to perform intersection


# In[8]:


set_1 = {10,20,30,40,50}
set_2 = {5,10,15,20,25,30,35}
set_1.intersection_update(set_2)
print(set_1)

# updates the value of the original set


# In[9]:


print(set_1)


# In[10]:


r = {"a","b","c","i","u","p","s","o"}
s = {"a","e","i","o","u"}
diff = r.difference(s)
print(diff)

# items in r that are not common in s get printed


# In[12]:


r = {"a","b","c","u","p"}
s = {"a","e","i","o","u"}
symdiff = r.symmetric_difference(s)
print(symdiff)

# prints uncommon items of both sets


# In[15]:


r = {"a","b","c","u","p"}
s = {"a","e","i","o","u"}
t = r - s
print(t)
u = s - r
print(u)

# - can be used for difference


# In[16]:


r = {"a","b","c","u","p"}
s = {"a","e","i","o","u"}
symdiff = r ^ s
print(symdiff)

# symmetric difference can be done by using ^ operator


# In[18]:


r = {7,18,10,45,1,96,11}
s = {7,9,11,13,15,17,19}
r.difference_update(s)
print(r)

# updates value of r after difference


# In[19]:


r = {7,18,10,45,1,96,11}
s = {7,9,11,13,15,17,19}
r.symmetric_difference_update(s)
print(r)

# updates value of r after symmetric difference


# In[20]:


x = {1,2,3,4,5}
y = {2,3,4}
z = y.issubset(x)
print(z)

# checks whether a set is a subset of another set


# In[21]:


x = {1,2,3,4,5}
y = {2,3,4}
z = y <= x
print(z)

# <= can be used for issubset


# In[23]:


seta = {11,15,20,24}
setb = {11,20}
ss = seta.issuperset(setb)
print(ss)

# checks whether a set is a superset of another set / returns whether the set came from a bigger set.


# In[24]:


seta = {11,15,20,24}
setb = {11,20}
ss = seta >= setb
print(ss)

# >= can be used for issuperset


# In[25]:


s1 = {13,15,16,17,18}
s2 = {13,516,1718}
dj = s1.isdisjoint(s2)
print(dj)

# checks if a set is disjoint (not common at all) to the other set


# In[26]:


s1 = {13,15,16,17,18}
s2 = {131,516,1718}
dj = s1.isdisjoint(s2)
print(dj)


# In[ ]:




