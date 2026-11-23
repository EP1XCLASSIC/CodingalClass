numbers = int(input("Enter how many numbers to sum: "))

totalsum = 0

i = 1

while i<=numbers:
    totalsum += i
    i += 1

print(f"\nThe sum of the natural numbers till number {numbers} is: {totalsum}")