#!/usr/bin/env python
# coding: utf-8

# In[18]:


# This code separates above average and below average scores (above average being 1050).
sat_scores = [1600,1250,580,600,1480,1080,900,960,1500,1160,500,1070,1090,1560,1250,1150,1390,1000,1050,1190,1170,1450,980,560,1300,1590,1450,1200,1250]
def sort_scores(lis):
    good_lis = []
    bad_lis = []
    if lis[i] > 1050:
        good_lis.append(lis[i])
    else:
        bad_lis.append(lis[i])
    print("Above average scores:\n ",good_lis)
    print("Below average scores: \n",bad_lis)
sort_dec(sat_scores)


# In[20]:


# This code prints all scores in descending order.
def dec_order(lis):
    for i in range(len(lis)):
            largest = i
            for j in range(i+1,len(lis)):
                if lis[j] > lis[largest]:
                    largest = j
            lis[i], lis[largest] = lis[largest], lis[i]
    print("All scores in descending order: \n",lis)
dec_order(sat_scores)


# In[ ]:




