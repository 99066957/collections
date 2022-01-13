list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists (list1, list2):
    print("---------")
    for i in range(10):
        add = list1[i] + list2[i]
        print(f"{list1[i]} + {list2[i]} = {add}")

def substractAndDisplayLists (list1, list2):
    print("---------")
    for i in range(10):
        add = list1[i] - list2[i]
        print(f"{list1[i]} - {list2[i]} = {add}")

def multiplyAndDisplayLists (list1, list2):
    print("---------")
    for i in range(10):
        add = list1[i] * list2[i]
        print(f"{list1[i]} x {list2[i]} = {add}")

def divideAndDisplayLists (list1, list2):
    print("---------")
    for i in range(10):
        add = list1[i] / list2[i]
        print(f"{list1[i]} : {list2[i]} = {add}")


addAndDisplayLists (list1, list2)
substractAndDisplayLists (list1, list2)
multiplyAndDisplayLists (list1, list2)
divideAndDisplayLists (list1, list2)

 