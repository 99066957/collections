import random

kleuren = ['oranje', 'blauw', 'groen', 'bruin']

def zakken(MM):
    zakmm = []
    for i in range(MM):
        zakmm.append(random.choice(kleuren))
    return zakmm

MM = int(input("Hoeveel M&M's wilt u toevoegen aan de zak?"))
zakmm = zakken(MM)
print(zakmm)
    


