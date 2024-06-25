#Take two int values from user and print greatest among them.

num1 = int(input("\nEnter 1st number : "))
num2 = int(input("\n Enter 2nd number : "))

if num1 > num2:
    print(f"\n{num1} is greater than {num2}.\n")
elif num1 == num2:
    print(f"\n{num1} & {num2} are equal.\n")
else:
    print(f"\n{num2} is greater than {num1}.\n")