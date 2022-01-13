dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag" ]

print("Alle dagen van de week zijn : ")
for i in range(len(dagen)):
    print(dagen[i])

print("Alle werkdagen zijn : ")
for i in range(5):
    print(dagen[i])

print("Alle weekend dagen zijn : ")
for i in range(5, 7):
    print(dagen[i])

print("Alle weekdagen omgekeerd zijn : ")
for i in range(6, -1, -1):
    print(dagen[i])

print("Alle weekenddagen omgekeerd zijn : ")
for i in range(6, 4, -1):
    print(dagen[i])
