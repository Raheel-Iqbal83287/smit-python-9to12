'''
Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible.
'''

age = int(input("Enter your age : "))

if age > 17:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")