print("This is an electricity bill calculator.")

electricityusage = float(input("\nEnter your electricity usage: "))

if electricityusage <= 50:
    electricitybill = electricityusage * 2.60 + 25
elif 100 >= electricityusage > 50:
    electricitybill = electricityusage * 3.25 + 35
elif 100 < electricityusage <= 200:
    electricitybill = electricityusage * 5.26 + 45
else:
    electricitybill = electricityusage * 8.45 + 75

print("\nYour electricity bill is: ", electricitybill)        