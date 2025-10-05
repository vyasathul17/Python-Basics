#!/usr/bin/env python
# coding: utf-8

# # Python quiz game

# In[1]:


questions = ("Who invented the telephone? :",
            "Which festival is known as the 'Festival of Lights'? :",
            "What is the name of the weak zone of the Earth's crust where tectonic forces cause earthquakes? :",
            "In 2019, which popular singer was awarded the Bharat Ratna award? :",
            "The 100 Rupee note in India is signed by the Governor of which institution? :")

options = (("A.Nikola Tesla","B.Thomas Edison ","C. Alexander Graham Bell ","D.Guglielmo Marconi "),
           ("A.Holi","B.Eid ","C.Christmas ","D.Diwali "),
           ("A.Seismic zone","B.Volcanic zone ","C.Tectonic plate ","D.Continental shelf "),
           ("A.Lata Mangeshkar","B.Asha Bhosle ","C.Bhupen Hazarika ","D.Manna Dey "),
           ("A.The Prime Minister","B.The Finance Minister ","C.The Reserve Bank of India (RBI) ","D. None of the above"))

answers = ("C","D","A","C","C")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
      print(option)

        

    guess = input("Enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct ansswer")
    question_num += 1


print("----------------------------")
print("         Results            ")
print("----------------------------")

print("answers: ",end = " ")
for answer in answers:
    print(answer, end=" ")

print("guesses:", end =" ")
for guess in guesses:
    print(guess, end =" ")

print()

score = int(score/ len(questions) * 100)
print(f"Your score is: {score}%")


# In[ ]:




