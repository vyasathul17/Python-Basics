#!/usr/bin/env python
# coding: utf-8

# # variable

# variable  = A container of values(string,integer,float,boolean)
# A variable behaves as if it was the value it contains

# Strings

# In[1]:


first_name = 'Athul'
print(first_name)


# In[3]:


print(f'Hello {first_name}')


# In[4]:


food = 'Pizza'
print(f'you like {food}')


# In[8]:


email = 'sasi@123.com'
print(f'your email is {email}')


# In[ ]:





# Integers

# In[9]:


age  = 25
print(f'You are {age} of old')


# In[10]:


quantity = 3
print(f'if you are going to buy{quantity} items')


# In[11]:


num_of_students = 30
print(f'Your class has {num_of_students} number of students')


# In[ ]:





# Float

# In[13]:


Price = 10.99
print(f'The price is ${Price}')


# In[15]:


distance = 5.5
print(f'You can run {distance}')


# In[ ]:





# Booleans

# In[19]:


is_students = False
print(f'Are you a students? :{is_students} ')


# In[20]:


if is_students:
    print('You are a student')
else:
    print('You are not a student')


# In[21]:


for_sale = True
if for_sale:
    print('That item is for sale')
else:
    print('That item is not for sale')


# In[22]:


is_online = True
if is_online:
    print('I m on online')
else:
    print('I m not on online')


# In[ ]:





# # Typecasting

# The process of converting a variable from one data type to another str(), int(), float(), bool()

# In[23]:


name = 'Rahul Nani'
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


# In[25]:


gpa = int(gpa)
print(gpa)
print(type(age))


# In[26]:


age = str(age)
print(age)
print(type(age))


# In[28]:


name = bool(name)
print(name)


# # Input

# input () - A function that prompts the user to ebter data return the entered data as string

# In[29]:


input('What is your name ?: ')


# In[30]:


name = input('What is your name?: ')
print(f'Hello {name}!')


# In[31]:


name  = input('What is your name ?: ')
age = input('How old are you?: ')
print(f'Hell {name} !')

print(f'you are {age} years old')


# In[32]:


name = input('What is your name ?: ')
age = input('How old are you ?: ')
age = int(age)
age =  age + 1

print(f'Hello {name}!')
print('Happy Birthday')
print(f'You are {age} years old ')


# In[33]:


name = input('What is your name ?: ')
age = int(input('How old are you ?: '))
age = age + 1 

print(f'Hello {name}!')
print('Happy Birthday')
print(f'You are {age} years old ')


# Exercise 1 Rectangle Area calculation

# In[38]:


length = float(input('Enter the length :'))
breath = float(input('Enter the breath :'))
area = length * breath

print(f'The are is: {area} cm')


# Exercise 2 shopping Cart program
# 

# In[39]:


item = input('what item would you like to buy :?')
price = float(input('what is the price ? :'))
quantity = int(input('How many would you like ?:'))

total = price * quantity
print(f'You have bought {quantity} x {item}/s')
print(f'Your total is: {total}')



# # Arithmatic operation

# In[40]:


friends = 0
friends = friends + 1
print(friends)


# In[41]:


friends += 1
print(friends)


# In[42]:


friends = friends - 2 
print(friends)


# In[50]:


friends -= 2
print(friends)

friends = friends * 3
print(friends)

friends *= 3
print(friends)

friends /=  2
print(friends)

friends = friends ** 2
print(friends)
friends **= 2
print(friends)


# In[51]:


Friend = 20
remainder = Friend % 2
print(remainder)


# In[56]:


x = 3.14
y = -4
z = 5
result = max(x,y,z)
# result = round(x)
# result = abs(y)
# result = pow(4,3)

print(result)


# In[57]:


import math


# In[58]:


print(math.pi)


# In[59]:


print(math.e)


# In[61]:


x = 9
result = math.sqrt(9)
print(result)


# In[63]:


y = 9.9
#result  = math.ceil(y)
print(result)


# In[64]:


result = math.floor(y)
print(result)


# calculating circumference of a circle
# 

# In[65]:


import math 

radius = float(input('Enter the radius of a cicle: '))
circumference = 2 * math.pi * radius

print(f'The circumference is: {circumference} ')


# In[68]:


radius = float(input('Enter the radius of the circle: '))
circumference = 2* math.pi * radius
print(f'The circumference is : {round(circumference,2)}')


# calculating Area of a circle

# In[67]:


import math 

radius = float(input('Enter the radius of the circle: '))
area = math.pi * pow(radius, 2)

print(f'The ares of the circle is: {area}cm^2')


# In[69]:


import math 

radius = float(input('Enter the radius of the circle :'))
area = math.pi * pow(radius,2)

print(f'The area of the circle is : {round(area,2)}')


# To find the Hypotenuse of a triangle 

# In[70]:


import math
a =  float(input('Enter side A: '))
b = float(input('Enter side B:'))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f'Side C = {c}')


# In[ ]:





# # If statement

# 'If' =  Do some code only if some condition is True 
# else do something else

# In[71]:


age  = int(input('Enter the age :'))

if age >= 18:
    print('You are now signed up!')


# In[73]:


age  = int(input('Enter the age :'))

if age >= 18:   
    print('You are now signed up!')
else:
    print('You must be 18+ to sign up')


# In[76]:


age  = int(input('Enter the age :'))

if age >= 18:   
    print('You are now signed up!')
elif age < 0:
    print('You haven been born yet!')
else:
    print('You must be 18+ to sign up')


# In[77]:


age  = int(input('Enter the age :'))

if age >= 18:   
    print('You are now signed up!')
elif age < 0:
    print('You haven been born yet!')
elif age >= 100:
    print('you are too old to sign up')
else:
    print('You must be 18+ to sign up')


# In[79]:


Response = input('Would you like food? (Y/N): ')

if Response == 'Y':
    print('Have some food!')
else:
    print('No food for you!')


# In[80]:


name = input('Enter your name: ')
if name == "":
    print('You did not type in your name!')
else: 
    print(f'Hello {name}')


# In[81]:


for_sale = True

if for_sale:
    print('This item is for sale')
else: 
    print('This item is not for sale')


# In[82]:


online = True

if online:
    print('This user is online')
else: 
    print('The user is offline')


# # Logical operators

#  logical operators (and,or,not) = used to check if two or more conditional statement is 

# In[3]:


temp = int(input('What is  the temperature outside?: '))

if temp >= 0 and temp <=30:
    print('The temperature is good today!')
    print('go outside')


# In[4]:


temp =  int(input('What is the temperature outside ?:'))

if temp >= 0 and temp <= 30:
    print('The temperatutre is good today!')
    print('go outside')
elif temp  < 0 or temp > 30:
    print('The temperature is bad today')
    print('Stay inside ')


# In[8]:


temp = int(input('What is the temperature outside ?:'))
if not(temp < 0 or temp > 30):
    print('The temperature is good today!')
    print('go outside')

elif not(temp >= 0 and temp <= 30):
    print('The temperature is bad outside!')
    print('stay inside ')
    


# # While loop

#  While loop =  a statement that will execute it's block of code ,
#               as long as its condition remains true
# 
# 

# In[13]:


# while 1 ==1:
   # print('Help: i am stuck in a loop!')


# In[16]:


name = ""
while len(name) == 0:
    name = input ('Enter your name: ')
print('Hello '+ name)


# In[17]:


name  = None
while not name :
    name = input('Enter your name: ')
print("Hello "+name)


# # for loop

#  For loop =  a satement that will execute its block of code a limited amount of times
# 
#  while loop = Unlimited
# 
#  for loop = limited

# In[18]:


for i in range(10):
    print(i)


# In[19]:


for i in range (10):
    print(i+1)


# In[22]:


# for i in range(50,100):
#    print(i)

# for i in range (50,100+1,2):
#    print(i)


# In[23]:


import time


# In[26]:


for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('Happy Diwali !')


# # Nested Loops

#  Nested loops = The "inner loop" will finish all of its iterations before
#                 finishing one iteration of the "outer loop"

# In[28]:


rows = int(input('How many rows?: '))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end= '')
    print()


# # conditional expression 

#  conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition 
# 
# 'X if condition else Y'

# In[1]:


num = 5
print( "Positive" if num  > 0 else "Negative" )


# In[2]:


num = 6
result = 'Even' if num % 2 == 0 else '0dd'
print(result)


# In[5]:


a = 6 
b = 7

max_num = a if a > b else b
min_num = a if a < b else b
print(min_num)
print(max_num)


# In[6]:


age = 25 
status = 'Adult' if age >= 18 else 'child'
print(status)


# In[3]:


temperature = 30
weather = 'Hot' if temperature  > 20 else 'Cold'
print(weather)


# In[4]:


user_role = 'admin'
access_level = 'Full Access' if user_role == 'Admin' else 'Limited access'
print(access_level)


# In[5]:


user_role = 'Guest'
access_level = 'Full Access' if user_role == 'Admin' else 'Limited Access'
print(access_level)


# In[ ]:




