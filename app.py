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
print("Welcome to the Tip calculator!")
bill = input("What was the total bill? $")
tip = input("what percentage tip would you like to give? 10, 12, or 15?")
percentage_tip = int((tip)) / 100 * float(bill) + float(bill)
print(f"your total about of Tip is ${percentage_tip}")
people = input("how many people will pay this bill?")
result = int(percentage_tip) / int(people)
fresult = "{:.2f}".format(result)
print(f"Each person would pay: ${fresult} \nThank you for your Patronage!!")