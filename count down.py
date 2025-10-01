#!/usr/bin/env python
# coding: utf-8

# # Count down timer program

# In[1]:


import time 

time.sleep(3)
print("Time's up!")


# In[2]:


my_time = int(input("Enter the time in seconds: "))

for i in range(0,my_time):
    time.sleep(1)
print("Time's up!")


# In[3]:


my_time = int(input("Enter the time in seconds: "))

for i in range (my_time,0,-1):
    print(i)
    time.sleep
print("Time's up !")


# In[4]:


my_time = int(input("Enter the time in seconds: "))

for i in range (my_time,0,-1):
    seconds = i % 60
    minutes = int(i/60)%60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(2)
print("Time's up !")


# In[ ]:




