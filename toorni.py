import readCSVs

hospitals = readCSVs.giveEMS()

for h in hospitals:
    print(h["NAME"])
