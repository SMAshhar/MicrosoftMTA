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

brithday = input("What is your birthday? (mm/dd/yyyy)")
birthdate = datetime.datetime.strptime(brithday, "%m/%d/%Y").date()
print(birthdate.day, birthdate.month, birthdate.year)

