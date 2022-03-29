strGroceryList ="Milk, Tea, Sugar, Salt, Almonds, Handwash, Shampoo, Facewash, Toothpaste"
print(strGroceryList[6:9])
lstGroceryList = strGroceryList.split(",") # Convert String into list separated by comma not space
print(lstGroceryList)
print(lstGroceryList[1][2])
lstGroceryList.append("Ginger")
print(lstGroceryList)
del(lstGroceryList[3])
print(lstGroceryList)

# Declaring list directly without converting from string
strMedicineList =["Hypericum","Avena Sativa","Allium Cepa","Acconite","Ledum Pal","Arnica","Nux Vomica","Opium"]
print(strMedicineList)
strMedicineList.sort()
print(strMedicineList)
strMedicineList.insert(3,"Gal B Tone")
print(strMedicineList)
del(strMedicineList[8])

# Joining Lists
strListAll = [strGroceryList , strMedicineList]
print(strListAll)
gameslist=["apex legend',callofduty warzone',spiderman',miles morales',horizon2',cold war"]
print(gameslist)