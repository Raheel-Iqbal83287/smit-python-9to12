#Take input of age of 3 people by user and determine oldest and youngest among them.

age1 = int(input("\n Enter age of Person 1 : "))
age2 = int(input("\n Enter age of Person 2 : "))
age3 = int(input("\n Enter age of Person 3 : "))

if (age1 > age2) and (age1 > age3):
    print("\nPerson '1' is oldest among three persons.")
    if age2 < age3:
        print("\nPerson '2' is youngest among three persons.\n")
    else:
        print("\nPerson '3' is youngest among three persons.\n")
elif (age2 > age1) and (age2 > age3):
    print("\nPerson '2' is oldest among three persons.")
    if age1 < age3:
        print("\nPerson '1' is youngest among three persons.\n")
    else:
        print("\nPerson '3' is youngest among three persons.\n")
elif (age3 > age1) and (age3 > age2):
    print("\nPerson '3' is oldest among three persons.")
    if age1 < age2:
        print("\nPerson '1' is youngest among three persons.\n")
    else:
        print("\nPerson '2' is youngest among three persons.\n")

