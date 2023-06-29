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
# import random
# user_choice = input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors")
#
# computer_choice = random.randint(0,2)
# print(f"Computer chose {computer_choice}")
#
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
# elif computer_choice > user_choice:
#     print("You lose")
# elif user_choice > computer_choice:
#     print("You win")
# elif computer_choice == user_choice:
#     print("its a draw")

############ Day 5 ####################333
#loop
# fruits = ["Apple", "Peach", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

#excercise
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# # 🚨 Don't change the code above 👆
#
# sum = sum(student_heights)
# average = len(student_heights)
# result = sum / average
# print(result)

#excercise 2
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#print(max(student_scores)) # easy way to do this



#Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is {highest_score}")

#loop range
# for number in range(1,11, 3):
#     print(number)
# total = 0
# for number in range(1,101):
#     total += number
#     print(total

#excercise adding even number
# total = 0
# for number in range(2,101, 2):
#     total += number
# print(number)

#excersise  FizzBuzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
##day 5 final assignment
#password project

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")

####Day 6 ####
# function
# def my_function():
#     print("hello world")
#     print("My name is roland Onabolujo")
#
# for intro in range(6):
#     my_function()

# indentation
#while loop

###### Day 7 ##############
#Step 1

# word_list = ["aardvark", "baboon", "camel"]
#
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#
# import random
# chosen_word = random.choice(word_list)
#
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#
# guess = input("Guess a letter: ").lower()
#
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
# #Step 3
#
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#
# guess = input("Guess a letter: ").lower()
#
# #Check guessed letter
# for position in range(word_length):
#     letter = chosen_word[position]
#     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter
#
# print(display)
#
# #Step 3
#
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# end_of_game = False
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     print(display)
#
#     #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
# #Step 4
#
# import random
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #Set 'lives' to equal 6.
# lives = 6
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1.
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives])

###### Day 8 #################
#functions with inputs
# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("Hello Roland ")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do{name}")
#
# greet_with_name("Roland")
## function with multiple inputs

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with("Roland", "Madison")