#!/usr/bin/env python
# coding: utf-8

# In[2]:


import statistics

def mean_num_friends(x):
    # TODO
    return statistics.mean(x)
        

def median_num_friends(x):
    # TODO
    return statistics.median(x)

num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean  =  " + str(mean_num_friends(num_friends)))
print("meadian  =  " + str(median_num_friends(num_friends)))


# In[ ]:




