'''
A school has following rules for grading system:

a. Below 25 - F

b. 25 to 45 - E

c. 45 to 50 - D

d. 50 to 60 - C

e. 60 to 80 - B

f. Above 80 - A

Ask user to enter marks and print the corresponding grade.
'''

marks = int(input("\nEnter your marks : "))

if marks < 25:
    print("\nYour grade is \'F\'.\n")
elif marks >= 25 and marks <= 45:
    print("\nYour grade is \'E\'.\n")
elif marks > 45 and marks <= 50:
    print("\nYour grade is \'D\'.\n")
elif marks > 50 and marks <= 60:
    print("\nYour grade is \'C\'.\n")
elif marks > 60 and marks <= 80:
    print("\nYour grade is \'B\'.\n")
elif marks > 80 and marks <= 100:
    print("\nYour grade is \'A\'.\n")