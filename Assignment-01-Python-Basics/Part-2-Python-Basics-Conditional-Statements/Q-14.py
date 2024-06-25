'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user

Number of classes held

Number of classes attended.

And print

percentage of class attended

Is student is allowed to sit in exam or not.
'''

classesHeld = int(input("\nEnter Number of classes held : "))

classesAttended = int(input("\nEnter Number of classes attended : "))

percentClassesAttended = round(classesAttended / classesHeld * 100,2)

if percentClassesAttended >= 75:
    print(f"\nPercentage of classes attended : {percentClassesAttended}")
    print("\nYou are allowed to sit in exam.\n")
else:
    print(f"\nPercentage of classes attended : {percentClassesAttended}")
    print("\nYou are not allowed to sit in exam. Because, your attendance is less than 75%.\n")