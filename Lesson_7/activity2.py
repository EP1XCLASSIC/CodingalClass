a = int(input("Enter your a variable: "))
b = int(input("Enter your b variable: "))
c = int(input("Enter your c variable: "))

if not a == b:
    print("They are different.")
if not a!=c:
    print("\nThey are the same.")
if a==b and b==c:
    print("\nAll the variables are the same.")            
if a>=40 and b>40 or c>40:
    print("\nIf you see this, then that means both a and b are greater than 40, but c may not be greater than 40.")