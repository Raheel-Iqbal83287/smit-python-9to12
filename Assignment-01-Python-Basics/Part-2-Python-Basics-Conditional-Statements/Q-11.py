'''
 A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
'''

quantity = int(input("\nEnter quantity purchased : "))

cost = quantity * 100

if cost > 1000:
    discount = cost * 0.10
    print(f"\nYour cost of purchased quantity is : {cost}")
    print(f"\nYou will receive 10% discount on cost of purchased quantity for Rs.{discount}.")
    print(f"\nYour cost of purchased quantity after discount is : Rs.", (cost-discount), "\n")
else:
    print(f"Your cost of purchased quanity is less than Rs.1000. Therefore, you will not recieve discount.")