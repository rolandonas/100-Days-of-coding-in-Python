# #1.1 printing
# print("Day 1 - Python Print Function")
# print("The function is declared like this")
# print("Print('what to print')")
#
# #1.2 string Manipulation
# print("Hello world!\nHello word!\nHello word!")
# print("Hello" + "Roland")
# print("Hello" +" "+ "Roland") # Adding space to the string
# #types of error Indentation error(space error) and syntax error (could be the quote)
# #1.3 Debugging
# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the '+' Sign.")
# print("'e.g'. print(Hello + World)")
# print("New lines can be created with a backslash and n,")
# #Input Function
# input("what is your name?")
# # I stored Roland in the input file so it returns HelloRoland
# print("Hello" +input("what is your name?"))
#Excercise
#A program that calculate the number of letters in a name
# input("Hey Dear, what is your name?")
# print(Len(input("Hey Dear, what is your name?")))
# input("What is your name?")
# print(len(input("what is your name?")))
#1.4 Python Variables
# Dont change the code below
# a = input("a:")
# b = input("b:")
#######################
#write your code here
# c = a
# a = b
# b = c
# print("a =" + b)
# print("b= " + a)
#1. Create a greeting for your program.
# print("Welcome to Roland studio generator.")
#2. Ask the user for the city that they grew up in.
# cityname = input("What city did you grow up in?\n")

#3. Ask the user for the name of a pet.
# petname = input("What is the name of your favourite pet?\n")
#4. Combine the name of their city and pet and show them their band name.
# print("Your band name should be:\n"  + cityname +  petname)
#5. Make sure the input cursor shows on a new line:

###################################  Day 2 ##################################################
#Data types
#string
# print("Hello"[4]) # To pull out a letter from zero

# print("123"+"345")

#integer
# print(123+345)

#float (floating point number)
# 3.14150

#Boolean
# True
# False

# num_char = len(input("what is your name?"))
#
# new_num_char = str( num_char )
# print("your name has" + " "+ new_num_char +" " + "Characters")  #adding a string to an integer wouldnt work
#Excercise
# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# first_number = two_digit_number[0]
# second_number = two_digit_number[1]
# result = (int(first_number) + int(second_number))
# print(result)
#Excercise BMI calculator
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Bmi = int(weight) / float(height) ** 2
# result = round(Bmi,3)  #round to round up number or use // to round up
# print(result)
#f-string print(f"my score is"{90})

#Excercice Your life in weeks

# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
# result = f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
# print(result)

#Excercise Tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# print("Welcome to the Tip calculator!")
# bill = input("What was the total bill? $")
# tip = input("what percentage tip would you like to give? 10, 12, or 15?")
# percentage_tip = int((tip)) / 100 * float(bill) + float(bill)
# print(f"your total about of Tip is ${percentage_tip}")
# people = input("how many people will pay this bill?")
# result = int(percentage_tip) / int(people)
# fresult = "{:.2f}".format(result)
# print(f"Each person would pay: ${fresult} \nThank you for your Patronage!!")

#####################Day 3###########
#If else statement
# print("welcome to Roland Rollercoster!")
# height = int(input("what is your height?"))
# if height >= 120:
#     print("you can ride the Rollercoster")
# else:
#     print("sorry, you have to grow tall before you can ride. eat more Beans I guess")

#Excersise 3.1 odd or even number
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if number % 2 == 0:
#     print("This ia a even number")
# else:
#     print("This is a odd Number")

# Excercise 3.2 nested if statement
# print("welcome to Roland Rollercoster!")
# height = int(input("What is your height?"))
# if height >= 120:
#     print("You can ride the Rollercoster")
#     age = int(input("what is your age?"))
#     if age < 12:
#         bill = 5
#         print("Toddler ticket $5.")
#     elif age <= 18:
#         bill = 7
#         print("Teenager ticket $7.")
#     elif age >=45 and age <= 55:
#         print("Everything is going to be okay. Have a free ride on us")
#     if age == 20:
#         bill = 12
#         print("Youth ticket $12.")
#     else:
#         bill = 20
#         print("Adult ticket $20.")
#
#     photo = input("Would you want to take a picture with an additional fee of $3? Y or N. " )
#     if photo == "Y":
#         bill += 3
#
#     print(f"your finall bill is ${bill}")

# else:
#     print("sorry, you have to grow tall before you can ride. eat more Beans I guess")

# Logical Operator
# Love Calculator
# 🚨 Don't change the code below 👇
# print("Welcome to Roland Love Calculator!")
# name1 = input("What is your full name? \n")
# name2 = input("What is their full name? \n")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
#
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
#
# true = t + r + u + e
#
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
#
#
# if (love_score) < 10 or (love_score > 90):
#  print(f"your Love score is {love_score}, You should start your Wedding preparation, Your are Perfect together!!")
#
# elif (love_score >= 40) and (love_score <= 50):
#  print(f"your score is {love_score}, You are alright together")
#
# elif (love_score >= 100):
#     print(f"your score is {love_score}, you go like Coke and mentos")
#
# else:
#  print(f"Your score is {love_score}")

#Excercise Treasure hurt
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')
# print("Welcome to Roland Tresure Island \nYour Mission is to find a treasure \nGoodluck!!!")
# choice_1 = input("you are at a crossroad, Where would you go Left or Right. Type Left or Right?").lower()
# if choice_1 == "left":
#     print("Congratulations!!!! Now we move to the next stage!!!")
#     choice_2 = input("you are in front of a lake what would you do? swim or wait?").lower()
#     if choice_2 == "wait":
#         print("Congratulations!!!! Now we move to the next stage!!! ")
#     else:
#         print("Game over you have been eaten by crocodies in the lake")
#
#     choice_3 = input("which door would you enter Red, Blue or Yellow").lower()
#     if choice_3 == "red":
#         print("you just entered a room of fire ")
#     elif choice_3 == "blue":
#         print("you have been eaten by a beast")
#     elif choice_3 == "yellow":
#         print("You Win")
#     else:
#         print("game over ")
#
# else:
#     print("Game over you fell inside a hole")

########## Day 4 ##########################
#Randomisation and Python Lists
import random
# random_interger = random.randint(1,5)
# print(random_interger)

# random_float = random.random()
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
#Excercise
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
# import random
#
# random_side = random.randint(0,1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

#list
# states_of_america = ["Delaware", "Madison", "Tennesse", "Florida"]
# print(states_of_america[1])

import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]

# person_who_will_pay = random.choice(names) #this is an easier options to getting it done
# print(person_who_will_pay + " is going to buy the meal today!")
#Exercise Treasure map

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# horzontal = int(position[0]) #2
# vertical = int(position[1]) #3
#
# map[vertical - 1] [horzontal - 1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
#excercise
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors")

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("its a draw")