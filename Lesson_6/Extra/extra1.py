waterusage = int(input("How much water do you use: "))
electricityusage = int(input("How much electricity do you use: "))

if waterusage <= 200:
    water_bill = waterusage + 50 * (waterusage / 40)
elif 200 < waterusage < 400:
    water_bill = waterusage + 100 * (waterusage / 60)
else: # waterusage >= 400
    water_bill = waterusage + 200 * (waterusage / 100)

if electricityusage <= 200:
    electricity_bill = electricityusage + 50 * (electricityusage / 40)
elif 200 < electricityusage < 400:
    electricity_bill = electricityusage + 100 * (electricityusage / 60)
else: # electricityusage >= 400
    electricity_bill = electricityusage + 200 * (electricityusage / 100)

print("The water bill is:", water_bill)
print("The electricity bill is:", electricity_bill)
print("The total expense is:", water_bill+electricity_bill)
