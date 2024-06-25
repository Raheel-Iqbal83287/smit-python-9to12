'''
Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR"
'''

age = int(input("\nEnter your age : "))

if age >= 20 and age <= 60:
    gender = input("\nEnter your gender (M or F) : ")
    maritalStatus = input("\nEnter your Marital Status (Y or N) : ")
    if gender == 'F':
        print("\nYou will work only in urban area.\n")
    elif gender == 'M' and (age >= 20 and age <= 60):
        if age >= 20 and age <= 40:
            print("\nYou may work in anywhere.\n")
        elif age > 40 and age <= 60:
            print("\nYou will work in urban areas only.\n")
else:
    print("\n\''ERROR\''\n")