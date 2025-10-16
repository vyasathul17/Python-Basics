#!/usr/bin/env python
# coding: utf-8

# # Python credit card validator program

# 
# 1. Remove any '-' or ' '
# 
# 2. Add all digits in the odd places from right to left
# 
# 3. Double every second digit from right to left.
# (If result is a two-digit number,
# add the two-digit number together to get a single digit.)
# 
# 4. Sum the totals of steps 2 & 3
# 
# 5. If sum is divisible by 10, the credit card # is valid

# In[5]:


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step1

card_number =  input("Enter a credit card #: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]
print(card_number)

#step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)


#step3

for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else: 
        sum_even_digits += x

# step 4
total = sum_odd_digits + sum_even_digits

#step5 

if total % 10 == 0:
    print("VALID")

else:
    print("INVALID")
    


# # Python Banking Program

# In[17]:


def show_balance(balance):
    print(f"Your balance is Rs{balance: .2f}")
    print("*********************")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")

    if amount < 0:
        print("That's not a valid amount ")
        return 0
      
    else:
        return amount
        
        
def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))
    print("*********************")

    if amount > balance:
        print("Insufficient funds")
        return 0
        print("*********************")
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0 
    else:
        return amount
        print("*********************")

def main():
        balance = 0 
        
        is_running = True
        
        while is_running:
            print("*********************")
            print("Banking program")
            print("*********************")
            print("1.Show Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            print("*********************")
        
            choice = input("Enter your choice (1-4): ")
        
            if choice == "1":
                show_balance(balance)
            elif choice == "2":
                balance += deposit()
            elif choice == "3":
               balance -= withdraw(balance)
            elif choice == "4":
                is_running = False
            else:
                print("*********************")
                print("This is not a valid choice")
                print("*********************")
        print("*********************")
        print("Thank you! have a nice day!")
        print("*********************")

if __name__ == '__main__':
   main()


# In[ ]:




