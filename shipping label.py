#!/usr/bin/env python
# coding: utf-8

# In[1]:


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    print()

    for value in kwargs.values():
        print(value,end = " ")


shipping_label("Dr","Moosa","Chakarvarthi","III",
              street = "123 chennai", 
              city = "Kunool",
             state = "Tamil nadu",
             zip = "54321")


# In[2]:


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('app')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')},{kwargs.get('zip')}")


shipping_label("Dr","Moosa","Chakarvarthi","III",
              street = "123 chennai", 
              city = "Kunool",
               app = "100f",
             state = "Tamil nadu",
             zip = "54321")


# In[3]:


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    print()

    if "app" in kwargs:
         print(f"{kwargs.get('street')} {kwargs.get('app')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('city')} {kwargs.get('state')},{kwargs.get('zip')}")


shipping_label("Dr","Moosa","Chakarvarthi","III",
              street = "123 chennai", 
              city = "Kunool",
               app = "100f",
               pobox = "mkld",
             state = "Tamil nadu",
             zip = "54321")


# In[ ]:




