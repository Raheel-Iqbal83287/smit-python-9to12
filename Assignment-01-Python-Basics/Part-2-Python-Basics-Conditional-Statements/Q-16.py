'''
Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
'''

year = int(input("\nEnter an year : "))

if (str(year)[-2:-1] == '0') and (year % 400 == 0):
    print(f"\n{year} is a leap year.\n")
elif (str(year)[-2:-1] != 0) and (year % 4 == 0):
    print(f"\n{year} is a leap year.\n")
else:
    print(f"\n{year} is not a leap year.\n")

