#opracht 1
from enum import nonmember

from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK
from operator import index
from selectors import SelectSelector

half = lambda x: x/2

print(half(6))

#opracht 2

def fibbonaciTillN (number: int):
    a = 0
    b = 1
    result =[]
    index = 0
    while number > 0:
        result.append(a+b)
        a = b
        b = result[index]
        number -= 1
        index+= 1
    return result

print(fibbonaciTillN(10))

#opdracht 3
#3/ schrijf een functie die een zin vraagt van de gebruiker, en die zin omzet als volgt:
# woorden in een even positie moeten in kleine letters, op een oneven positie moeten in hoofdletters.
# input: 'Dit is een erg korte zin' => DIT is EEN erg KORTE zin

zin = input("give a sentence")
words = zin.split()

index = 0
resultaat = []

for word in words:
    if index % 2 == 0:
        resultaat.append(word.upper())
        index += 1
    else:
        resultaat.append(word.lower())
        index += 1


print(" ".join(resultaat))


#opdracht 4
#Schrijf een functie sort(v1, v2, v3, v4) -> (float, float, float, float)
#die de input waarden gesorteerd retourneert.

def sort(v1, v2, v3, v4):
    list = [v1, v2, v3, v4]
    newList = []
    while list:
        newList.append(min(list))
        list.remove(min(list))
    return newList

print(sort(55, 95, 45,88))


#opdracht 5
#5/ Uitdaging: Werk deze functie correct uit
#  def divide_20_50(amount:float)-> (bool, int, int):
#  Als het input-bedrag opdeelbaar is in briefjes van 20 en 50 dan return True, count_50, count_20
#  anders False, None, None

def divide_20_50(amount:float)-> (bool, int, int):
    ispossible = True
    amount20 = 0
    amount50 = 0
    if amount %20 == 0:
        ispossible = True
        if amount > 100:
            amount50 = amount // 50
            amount20 = (amount%50)/20
        else:
            amount20 = amount // 20
    elif (amount - 50) % 20 == 0:
        amount50 = 1
        amount = amount - 50
        if amount > 100:
            amount50 += amount // 50
            amount20 = (amount%50)/20
        else:
            amount20 = amount // 20
    else:
        imispossible = False
        amount20 = None
        amount50 = None

    return(ispossible, amount20, amount50)

print(divide_20_50(3540))
print(divide_20_50(3550))
print(divide_20_50(3590))
print(divide_20_50(3555))



