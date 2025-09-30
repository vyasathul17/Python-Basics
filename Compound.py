#!/usr/bin/env python
# coding: utf-8

# # Python compound interest calculator

# In[1]:


principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Enter the principle amount: '))
    if principle <= 0:
        print("principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in Year's: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")


total = principle * pow((1+ rate/100),time)
print(f"Balance after {time} year/s: Rs{total:.2f}")


# In[2]:


principle = 0
rate = 0
time = 0

while principle < 0:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")

while rate < 0 :
    rate = float(input("Enter the interest rate "))
    if rate < 0:
        print("Rate can't be less than zero")

while time < 0 :
    time = int(input("Enter the time in years "))
    if time <0:
        print("Time cannot be less than zero")

total = principle *  pow((1 + rate/100), time)
print(f"Balance after {time} year/s : Rs{total: .2f}")


# In[3]:


principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True :
    rate = float(input("Enter the interest rate "))
    if rate < 0:
        print("Rate can't be less than zero")
    else:
        break

while True :
    time = int(input("Enter the time in years "))
    if time <0:
        print("Time cannot be less than zero")
    else:
        break

total = principle *  pow((1 + rate/100), time)
print(f"Balance after {time} year/s : Rs{total: .2f}")


# initial values don’t matter anymore because you’re using while True loops


# In[ ]:




