'''
Write a program to calculate the electricity bill (accept number of units from user) according to the following criteria : 

.Unit Price upto 100 units no charge Next 200 units Rs 5 per unit. 
.After 200 units Rs 10 per unit. 

(For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750.
'''

units = int(input("\nEnter number of units of electricity : "))

bill = 0

if units <= 100:
    bill = units * 0
    print(f"\nTotal bill amount is Rs.{bill}.\n")
elif units > 100 and units <= 200:
    bill = units * 5
    print(f"\nTotal bill amount is Rs.{bill}.\n")
elif units > 200:
    bill = units * 10
    print(f"\nTotal bill amount is Rs.{bill}.\n")