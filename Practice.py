# import datetime
# currentDate = datetime.date.today()
# print(currentDate)
# print(currentDate.year)
# print(currentDate.month)
# print(currentDate.day)
# print(currentDate.strftime('I have been working since %a, %dth of %b,%y'))
# asd = datetime.date(2050, 8, 29)
# print(asd.strftime("Yeehaw... Join Us on %dth of %B, %Y for a lovely evening"))
# print(asd.strftime("THe thing is %d of %B is our last chance to do anything. After that, the year %Y will no longer be valid for us"))
# print(asd.strftime("Yes Mirha is right, she called abba to everyone.... "))

import datetime

# x = input("DAte")
# y = datetime.datetime.strptime(x, "%m/%d/%Y")
# print(y.strftime("%m-%d-%Y"))

y = input("Enter your birthday")
birthdate = datetime.datetime.strptime(y, "%m/%d/%Y").date()
if birthdate.strftime("%d") == "02":
    print(birthdate.strftime("Your birthday will be on %dnd of %B, %Y" ))
elif birthdate.strftime("%d") == "01":
    print(birthdate.strftime("Your birthday will be on %dst of %B, %Y" ))
else:
    print(birthdate.strftime("Your birthday will be on %dth of %B, %Y" ))

