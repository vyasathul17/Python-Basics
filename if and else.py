#!/usr/bin/env python
# coding: utf-8

# Validate user input exercise
# 
# 1.username is no more than 12 characters
# 
# 2.username must not contain space
# 
# 3.username must not contain digits

# In[1]:


user_name = input("Enter a username: ")

if len(user_name) > 12:
    print('Your user name cant be more than 12 character')
else: 
    print(f'welcome {user_name}')


# In[2]:


user_name = input("Enter a username: ")
user_name.find(' ')

if len(user_name) > 12:
    print('Your user name cant be more than 12 character')
elif not user_name.find(' ') == -1:
    print('Your user name cant contain space')
elif not user_name.isalpha():
    print("your user name can't contain digit ")
else: 
    print(f'welcome {user_name}')


# In[ ]:




