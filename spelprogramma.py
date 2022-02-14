import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo' ]

def spelProgramma(spelList, minimum, maximum):
    r = random.choice(range(minimum, maximum))
    for i in range(r):
        print(random.choice(spelList))
              
spelProgramma(spelList, 2, 7)












