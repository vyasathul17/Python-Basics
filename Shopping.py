#!/usr/bin/env python
# coding: utf-8

# # Shopping cart exercise

# In[1]:


food = []
prices =[]
total = 0

while True:
    food = input("Enter a fruit to buy(q to quit):")
    if food == "q":
        break


# In[2]:


food = []
prices = []
food = 0
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break


# In[4]:


foods = []
prices = []
total = 0


while True:
    food = input("Enter a food to buy (q to quit )")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: Rs"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART------")


for food in foods:
    print(food, end = " ")

for price in prices:
    total += price
print()
print(f"Your total is :Rs{total}")


# In[5]:


total = 0
cart = []

while True:
    food = input("Enter a food to buy (q to end)")
    if food.lower() == "q":
        break

    else:
        price = float(input("Enter the price of {food}: Rs"))
        cart.append((food,price)) # store as a tuple (food, price)

print("--------YOUR CART-------")

for food,price in cart:
    print(f"{food} - Rs{price}")
    total += price

print(f"\nYour total is : Rs{total}")


# In[ ]:




