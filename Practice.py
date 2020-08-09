############################################ DATE TIME ########################################



# import datetime
# currentDate = datetime.date.today()
# print(currentDate)
# print(currentDate.year)
# print(currentDate.month)
# print(currentDate.day)
# print(currentDate.strftime('I have been working since %a, %dth of %b,%y'))
# # asd = datetime.date(2050, 8, 29)
# # print(asd.strftime("Yeehaw... Join Us on %dth of %B, %Y for a lovely evening"))
# # print(asd.strftime("THe thing is %d of %B is our last chance to do anything. After that, the year %Y will no longer be valid for us"))
# # print(asd.strftime("Yes Mirha is right, she called abba to everyone.... "))

# import datetime

# x = input("DAte")
# y = datetime.datetime.strptime(x, "%m/%d/%Y")
# print(y.strftime("%m-%d-%Y"))

# y = input("Enter your birthday")
# birthdate = datetime.datetime.strptime(y, "%m/%d/%Y").date()
# if birthdate.strftime("%d") == "02":
#     print(birthdate.strftime("Your birthday will be on %dnd of %B, %Y" ))
# elif birthdate.strftime("%d") == "01":
#     print(birthdate.strftime("Your birthday will be on %dst of %B, %Y" ))
# else:
#     print(birthdate.strftime("Your birthday will be on %dth of %B, %Y" ))


# birthday = datetime.datetime.strptime("5/14/2020", "%m/%d/%Y").date()
# print(birthday)
# todayDate = datetime.date.today()
# difference = todayDate - birthday
# print(difference.days)

# import datetime

# BD = input("Please enter your Birthday in format dd/mm/yyy")
# user_birthday = datetime.datetime.strptime(BD, "%d/%m/%Y")

# def daysCalculator():
#     currentDate = datetime.date.today()
#     difference = currentDate - user_birthday
#     print("You are now ", difference.days * 3600 * 24, " seconds older")
#     return difference.days * 3600 * 24

# x = user_birthday + datetime.timedelta(days = 15)
# x = user_birthday + datetime.timedelta(days = 3, hours = 15, minutes = 32, seconds = 43)
# print(x)

import datetime

# currentTime = datetime.datetime.now()
# x = datetime.datetime.strftime(currentTime, ("Right now, the time is %I: %m: %S %p on %d of %B, %Y"))
# print(x)

# x = input("Enter date in dd/mm/yyyy formate")
# deadline = datetime.datetime.strptime(x, "%d/%m/%Y")
# print(deadline)

# y = datetime.datetime.today()
# time = deadline - y
# print(time.days//7, " weeks ", time.days%7, " days ")

# z = input("Enter your date of deadline enter in formate, dd/mm/yyyy")
# deadline = datetime.datetime.strptime(z, "%d/%m/%Y")
# time = deadline - datetime.datetime.today()
# print(time.days//7, " weeks and ", time.days%7, " days")

#################################### EXCEPTIONS #############################################

# a = float(input("Enter first number"))
# b = float(input("Enter second number"))

# import sys

# try:
#     print(a, "/", b, " = ", a/b)
# except:
#     print("Nice.... a mistake. Always loves to make mistake")
#     print(sys.exc_info()[0])

# try:
#     print(a, "/", b, "=", a/b)
# except ZeroDivisionError:
#     print("Nom nom nom nom noooooommm.... !")

# import sys
# errorflag = False

# try:
#     print(int(a/b))
# except:
#     print("nope")
#     print(sys.exc_inf()[0])
#     errorflag = True
# if not errorflag:
#     print("No error found")

# import sys

# x = input("Enter the name of the file")
# try:
#     with open(x, "r") as f:
#         reader = f.reader
#         print(reader)
# except:
#     print("No file found")
#     print(sys.exc_info()[0])

# with open("A.txt", "w") as f:
#     f.write("Aloo tinde bangon")
# with open("A.txt", "r") as f:
#     x = f.read()
#     print(x)

################################# Writing Fil #####################################3

# x = 1

# while x <= 5:
#     y = input("Enter your guest name")
#     z = input("Enter their age")
#     with open("asd.csv", "a") as f:
#         f.write(f"{y}, {z}\n")
#     x += 1
# x = open("asd.csv", "r") 
# # y = x.read()
# # print(y)
# import csv

# def writer(filename, content):
#     with open(filename, "a") as f:
#         f.write(content)

# asd = "All is lost"
# writer("A.txt", asd)
# with open("A.txt", "r") as f:
#     print(f.read())

################################## File reader ################################
 
# import csv

# files = []
 
# with open("asd.csv") as f:
#     content = csv.reader(f)
#     for x in content:
#         files += x
#     print(files)    

# x = "20" * 3
# print(type(+1E10))

# L = int(input("Enter loan amount"))
# i = (int(input("Enter interest rate in % ")))/100
# n = int(input("Enter numbe rof years for installament"))

# M = L*(i*(1+i)*n) / ((1+i)*n-1)

# print("Your monthly installment is ", M)

# user = ""
# listOfUsers = []
# while user.lower() != "q":
#     user = input("Enter the name of guest or 'q' to quite")
#     if user.lower() != "q":
#         listOfUsers.append(user.title())
# listOfUsers.sort()
# print(listOfUsers)
# for users in listOfUsers:
#     print(users)
    
#######################  PLAYING WITH VARIABLES ##################

# print('''
#     This is your story. A story that was never yours - yet, you would want it to.
#     Enjoy .. !
# ''')

# name = input("Enter your name : ")
# favAnimal = input("Enter the name of your spritual animal : ")

# print(f"""
#     Like every morning, {name} woke up dizzy headed, yet there was 
#     some thing off about this morning. The light was too bright for
#     example or the wind was pleasently cold or {name} was not on bed.
    
#     Realizing the situation, {name}, that is you, got up in an instent,
#     eyes wide, to found yourself in a flowery meadow. Awestruck, you
#     glared around and found a {favAnimal}, staring right at you. A
#     bit starteled you got on your feet.

#     "Thats quite the get up you have there. " said te {favAnimal}
#     You realized that you are still wearing your pajamas, with the
#     tag {name} you got from your grandmother. 
#     """)

# color = input("Enter your fav. color : ")
# animal  = input("Enter your fav. animal : ")
# building  = input("Enter your fav. building : ")



# input("Hickery Dickery Doc..")
# input(f"A {color} {animal} went up the {building}")
# input("The clock struck one...")
# input(f"The {color} {animal} came down.")
# input("Hickery Dickery Doc..")

# import turtle
# turtle.forward(100)
# x = 0
# while x <= 4:
#     turtle.forward(100)
#     turtle.right(90)
#     x += 1
# input()

# import turtle
# turtle.color("blue")
# turtle.shape("turtle")
# turtle.circle(100)
# turtle.exitonclick()

# import os

# def reader(filename, mode):
#     with open(filename, mode) as f:
#         if os.path.isfile(filename):
#             return f.readlines()
#         else:
#             return None
# read = reader("A.txt", "r")
# for x in read:
#     print(x)
# print(read)

# print(type(5.0))

# a = [1, 2, 3]       
# b = ['a', 'b', 'c']
# print(a is b)
# print(a == b)
# a = b
# print(a is b)
# print(a == b)

# for x in range(2,12, 2):
#     for y in range(2,13):
# #         print(x, "*", y, " = ", x*y )
# i = 250 
# while len(str(i)) > 72: 
#     i *= 2 
# else: 
#     i //= 2 
#     print(i)

# n = 0 
# while n < 4: 
#     n += 1
#     print(n, end=" ")

# Val = 1 
# Val2 = 0 
# Val = Val ^ Val2 
# Val2 = Val ^ Val2 
# Val = Val ^ Val2
# print(Val)

# z, y, x = 2, 1, 0 
# x, z = z, y 
# print(x, y, z)
# y = y - z 
# # put line here 
# x, y, z = y, z, x
# print(x, y, z)

# a = 0 
# b = a ** 0 
# if b < a + 1: 
#     c = 1 
# elif b == 1: 
#     c = 2 
# else: 
#     c = 3 
# print(a + b + c)

# i = 10 
# while i > 0 : 
#     i -= 3 
#     print("*") 
#     if i <= 3: 
#         break 
#     else: 
#         print("*")

# for i in range(1, 4, 2): 
#     print("*", end="**")
# print("***")

# s = "Hello, Python!" 
# print(s[-14:19])

# lst = ["A", "B", "C", 2, 4] 
# del lst[0:-2] 
# print(lst)

# dict = { 'a': 1, 'b': 2, 'c': 3 } 
# for item in dict: 
#     print(item)

# s = 'python' 
# for i in range(len(s)): 
#     i = s[i].upper() 
# # print(s, end="")

# lst = [i // i for i in range(1,4)]
# print(lst)


# lst = [[c for c in range(r)] for r in range(3)] 
# for x in lst: 
#     for y in x: 
#         if y < 2: 
#             print('*', end='')

# lst = [2 ** x for x in range(0, 11)] 
# # print(lst[-1])

# lst1 = "12,34" 
# lst2 = lst1.split(',') 
# # print(len(lst1) < len(lst2))

# def fun(a, b=0, c=5, d=1): 
#     return a ** b ** c 
# print(fun(b=2, a=2, c=3))

# x = 5 
# f = lambda x: 1 + 2 
# print(f(x))

# from math import pi as xyz # line 01 
# print(xyz)

# import random
# for i in range(10): 
#     print(random(1, 5))

# x = 1 # line 1 
# def a(x): # line 2 
#     return 2 * x # line 3 
# x = 2 + a(x) # line 4 
# # print(a(x))

# s = 'SPAM' 
# def f(x): 
#     return s + 'MAPS' 
# print(f(s))


# def gen(): 
#     lst = range(5) 
#     for i in lst: 
#         yield i*i 
# for i in gen(): 
#     print(i, end="")

# import math
# def area_circle(r):
#     print(math.pi*math.pow(r,2))
# # area_circle(1)

# score = {"Dave":100000,
# "Steve":90000,
# "Amy":75900,
# }
# for person, score in score.items():
#     print('{0:8} *** {1:,}'.format(person, score))

# import sys
# print(sys.executable)

# x = 3
# x += 1
# x **=2
# print(x)


# x = 10
# y = 6

# z = y // 3 * 3 / 2 + x % 2 ** 2
# print(z)

# a = "True"
# b = "True"
# result = a is b
# print(result)

x = "Syed Muhammad Ashhar"
print(x[::-1])

rooms = {1:"foyer", 2:"conference room"}
room = int(input("enter the room number"))
if not room in rooms:
    print("Room doesnt exist")
else:
    print("your room name is: "+ rooms[room])