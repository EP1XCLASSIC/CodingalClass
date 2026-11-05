print("This is a BMI calculator (Kg/m^2).")

height = float(input("\nInput your height (m): "))
weight = float(input("Input your weight (Kg): "))

bodymassindex = int(weight / (height**2))

if bodymassindex <= 18.4:
    print("\nYou are underweight and your BMI is: ",bodymassindex)
elif 18.5 <= bodymassindex <= 24.9:
    print("\nYou are fit and your BMI is: ",bodymassindex)
elif 25 <= bodymassindex <= 29.9:
    print("\nYou are overweight and your BMI is: ",bodymassindex)
elif 30 <= bodymassindex <= 34.9:
    print("\nYou are severely overweight and your BMI is: ",bodymassindex)
else:
    print("\nYou are obese and your BMI is: ",bodymassindex)