char = input("Enter a character: ")

if len(char) == 1 and (('a' <= char <= 'z') or ('A' <= char <= 'Z')):
    print(f"'{char}' is an alphabet.")
else:
    print("Invalid input. Please enter a single alphabet character.")