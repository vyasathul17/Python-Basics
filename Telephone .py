#!/usr/bin/env python
# coding: utf-8

# # Telephone number-pad exercise

# In[1]:


num_pad = ((1 ,2 ,3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))


for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()


# In[ ]:




