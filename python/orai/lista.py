# lista = []
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[-1])
# for fruit in fruits:
#     print(fruit)
# for i in range(1,5+1):
#     print(i)
# print(fruits[2:4])
# lista = []
# lista1 = [1,4,5,3,6,2]

# for i in lista1:
#     print(i)
# print(lista1[-1])
# print(len(lista1)) #hosszúság

# szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# szamok[0] = szamok[2]
# print(szamok)
# kozepso = szamok[0:3]
# print(kozepso)
# utolso_harom = szamok[-3:]
# print(utolso_harom)

# lista = [1, 2, 3]
# lista.append(4)
# print(lista)

# lista = ["január", "február"]
# lista.append("március")
# print(lista)

# lista = [1, 2, 3]
# lista.extend([4, 5, 6])
# print(lista)

# lista = [1, 2, 3, 4, 5, 6]
# lista.insert(4, 10)
# print(lista)

# lista = [1, 2, 3, 2, 4]
# lista.remove(2)
# print(lista)
# lista.remove(2)
# print(lista)

# lista = [1, 2, 3, 4]
# elem = lista.pop()
# print(elem)  # 4
# print(lista)
# elem = lista.pop(2)
# print(elem) #3
# print(lista)

# lista = [1, 2, 3, 2, 4]
# index = lista.index(3) # hanyadik helyen van, indexen
# print(index)

# lista = [1, 2, 3, 2, 4, 2]
# db = lista.count(2)
# print(f"A 2-es elem {db}-szor fordul elő a listában.")

# feladat
# számold meg h a foci meccsen hány nyert vesztett és don tetlen meccs volt 
# ['ny', 'ny', 'v', 'd', 'd', 'd', 'v', 'v', 'ny', 'ny', 'd']
# győzelem 3 pontot ér a döntetlen egyet
# ird ki h hány pontja van a bajnokságban

# eredmenyek = ['ny', 'ny', 'v', 'd', 'd', 'd', 'v', 'v', 'ny', 'ny', 'd']
# gyozelemdb = eredmenyek.count('ny')
# dontetlendb = eredmenyek.count('d')
# print(f"A pontszám: {gyozelemdb*3+dontetlendb} pont")

# feladat 2
# iskolai verseny ahol pontokat kaptak a feladatok alapján
# ['jó', 'kitűnő', 'jó', 'közepes', 'kitűnő', 'kitűnő', 'jó', 'közepes', 'jó', 'kitűnő']
#kitűnő 5pont, jó 3pont, közepes 1pont 
#ha minden kitűnő lenne hány pont lenne?

# eredmenyek = ['jó', 'kitűnő', 'jó', 'közepes', 'kitűnő', 'kitűnő', 'jó', 'közepes', 'jó', 'kitűnő']
# print(f"Kitőnű eredmenyek esetén a pontszám: {len(eredmenyek)*5} pont lenne.")

# db = eredmenyek.count('kitűnő')
# print(f"A kitűnő eredmény {db} db")
# db = eredmenyek.count('jó')
# print(f"A jó eredmény {db} db")
# db = eredmenyek.count('közepes')
# print(f"A közepes eredmény {db} db")

# rendezett_lista = []
# for i in range(len(eredmenyek)):
#     db=0
#     if eredmenyek[i] not in rendezett_lista:
#         for j in eredmenyek:
#             if eredmenyek[i] == j:
#                 db+=1
#         print(f"A {eredmenyek[i]} eredményből, {db} van.")
#         rendezett_lista.append(eredmenyek[i])

# scores = [15, 25, 9, 35]
# students = ["Jane", "Amber", "Mark", "Todd", "Sandy"]
# print(students[1])
# print(scores[1])
# for score in scores:
#     print(score)
# print(has_robert)
# students.append("Robert")
# print("A tanulók száma: ",len(students))
# has_robert = "Robert" in students
# if has_robert:
#     print("Robert benne van a tanulók listájában.")
# else:
#     print("Robert nincs benne a tanulók listájában.")
# students.insert(0, "Steve")
# students.remove("Sandy")
# new_students = ["Kevin", "Ben", "Carla"]
# print("Új tanulók elött: ", len(students))
# students.extend(new_students)
# print("Új tanulók után: ", len(students))
# for student in students:
#     print(student)

# students = ["Jane", "Amber", "Mark", "Todd", "Sandy"]
# answers = ["A", "C", "C", "B", "B", "A"]
# grades = [5, 4, 1, 2, 4, 3, 2, 4, 5, 5]
# while "C" in answers:
#     answers.remove("C")
# firsItem = answers.pop(0)
# lastItem = answers.pop()
# print("Index: ", students.index("Mark")+1)
# print("Original:", students)
# students.sort()
# print("Sort:", students)
# students.reverse()
# print("Reverse:", students)
# students.clear()
# print("Clear:", students)
# print("B betűk száma: ",answers.count("B"))
# print("First item: ", firsItem, "Last item: ", lastItem)
# print("1-esek száma: ", grades.count(1))
# print("2-esek száma: ", grades.count(2))
# print("3-asek száma: ", grades.count(3))
# print("4-esek száma: ", grades.count(4))
# print("5-ösök száma: ", grades.count(5))
# print(answers)

import datetime as dt
dates = [
    dt.date(2024,9,29),
    dt.date(2024,9,30),
    dt.date(2024,9,28),
    dt.date(2024,9,17)
]
dates.append(dt.date(2024,9,22))
dates.sort()
for date in dates:
    print(date)
