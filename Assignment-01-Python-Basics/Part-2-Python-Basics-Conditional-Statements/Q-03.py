#Write a program to check whether a number entered by user is even or odd.

number = int(input("\nEnter a number to check is even or odd : "))

if number > 0:
    if number % 2 == 0:
        print(f"\n{number} is even.\n")
    else:
       print(f"\n{number} is odd.\n")
elif number == 0:
    print("\nYou entered 0. Please enter a postivie number.\n")
else:
    print("\nYou entered a negative number. Please enter a postivie number.\n")
