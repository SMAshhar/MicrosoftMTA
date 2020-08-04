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

print('''
    This is your story. A story that was never yours - yet, you would want it to.
    Enjoy .. !
''')

name = input("Enter your name : ")
favAnimal = input("Enter the name of your spritual animal : ")

print(f"""
    Like every morning, {name} woke up dizzy headed, yet there was 
    some thing off about this morning. The light was too bright for
    example or the wind was pleasently cold or {name} was not on bed.
    
    Realizing the situation, {name}, that is you, got up in an instent,
    eyes wide, to found yourself in a flowery meadow. Awestruck, you
    glared around and found a {favAnimal}, staring right at you. A
    bit starteled you got on your feet.

    "Thats quite the get up you have there. " said te {favAnimal}
    You realized that you are still wearing your pajamas, with the
    tag {name} you got from your grandmother. 
    """)



 