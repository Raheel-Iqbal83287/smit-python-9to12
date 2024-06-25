#Write a program to display the last digit of a number.

number = input("\nEnter a number : ")

if len(number) >= 2:
    print(f"The last digit of {number} is : ", number[-1])
else:
    print("\nYou entered a single digit number. Please enter a number of more than 1 digit.\n")