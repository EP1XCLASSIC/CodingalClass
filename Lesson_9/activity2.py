string = input("Input your string: ")

emptystring = ""

for i in string:
    emptystring = i + emptystring
print("\nYour original string was: ", string)  
print("Your reversed string is: ", emptystring)