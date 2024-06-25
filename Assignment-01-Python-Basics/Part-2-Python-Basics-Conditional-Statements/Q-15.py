'''
Modify the question 14 to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
'''

classesHeld = int(input("\nEnter Number of classes held : "))

classesAttended = int(input("\nEnter Number of classes attended : "))

percentClassesAttended = round(classesAttended / classesHeld * 100,2)

if percentClassesAttended >= 75:
    print(f"\nPercentage of classes attended : {percentClassesAttended}")
    print("\nYou are allowed to sit in exam.\n")
elif percentClassesAttended < 75:
    medicalCause = input("\nDo you have medical cause or not 'Y' or 'N' : ")    
    if medicalCause == 'Y' or medicalCause == 'y':
        print(f"\nPercentage of classes attended : {percentClassesAttended}")
        print("\nYou are allowed to sit in exam. Because, you have medical issue. However, your percentage of classes attended is less than 75%.\n")
    else:
        print(f"\nPercentage of class attended is {percentClassesAttended} & you don't have medical issue. Therefore, you are not allowed to sit in exam. Because, your attendance is less than 75%.\n")