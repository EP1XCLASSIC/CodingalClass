num = int(input("Enter your number: "))

totalsum = 0

copy = num

while copy > 0:
    digit = copy % 10
    totalsum += digit**3
    copy = copy // 10

if num == totalsum:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")  