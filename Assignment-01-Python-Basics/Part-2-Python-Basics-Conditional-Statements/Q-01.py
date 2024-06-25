'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
'''

salary = int(input("Enter your salary : "))
yearsOfService = int(input("Enter your Years of Service : "))
bonusAmount = 0

if yearsOfService > 5:
    bonusAmount = salary * 0.05
    print(f"Your bonus amount is : {bonusAmount}")
else:
    print("Your years of service are not more than 5 years. Therefore, you are not eligible for bonus.") 