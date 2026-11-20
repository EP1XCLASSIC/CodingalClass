#For loop for calculating sum of whole numbers in a range entered by user.
n = int(input("Enter the number for how long you want to repeat the sum (>1):"))

sumtotal = 0


for i in range(n+1):
    sumtotal = sumtotal + i
print("\nThe sum of the whole numbers:", sumtotal)