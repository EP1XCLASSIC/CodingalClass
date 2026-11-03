costprice = float(input("Enter how much you bought the item for: "))

sellingprice = float(input("Enter your selling price: "))

if sellingprice >= costprice:
    print("You have a profit of :", sellingprice - costprice)

else:
     print("You have a loss of :", costprice - sellingprice)    