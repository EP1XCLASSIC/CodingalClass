print("This is a program that checks your eligibility for a exam.\n")

medicalcause = bool(input("Enter 1 or 0 if you have a medical cause to give this exam or not: "))
attendance = float(input("\nEnter your attendance: "))

if medicalcause == True:
    print("\nYou are allowed to give the exam.")
else:
    if attendance >= 75:
        print("\nYou are allowed to enter the exam.")
    else:
        print("\nYou are not allowed to enter the exam.")