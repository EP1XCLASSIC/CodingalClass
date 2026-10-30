ammount = int(input("Enter the ammount: "))

note_1 = ammount//100

note_2 = (ammount%100)//50

note_3 = ((ammount%100)%50)//10

note_4 = (((ammount%100)%50)%10)

print("\nThe notes you need are: \n", note_1,"100 rs notes\n", note_2, "50 rs notes\n", note_3, "10 rs notes\n", note_4, "1 rs notes")