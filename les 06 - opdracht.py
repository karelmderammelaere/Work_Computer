# opdracht 1: schrijf een functie uniq(lst: list) -> bool die controleert
# of een gegeven lijst dubbele waardes bevat
# Voor wie al meer python kent: je mag hiervoor geen set gebruiken.
# uniq([]) -> False
# uniq([1,2]) -> False
# uniq([1,2,1]) -> True
# uniq(['A','B','A'])-> True
# uniq(['A','B','C'])-> False
from os import remove


def uniq(lst: list) -> bool:
    for i in range(len(lst)):
        j = i + 1
        while j < len(lst):
            if lst[i] == lst[j]:
                return True
            j += 1
    return False

print(uniq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(uniq([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]))

# opdracht 2:
# Je hebt een dictionary met punten voor verschillende vakken.
grades = {
    "wiskunde": 7.5,
    "nederlands": 8.0,
    "geschiedenis": 6.5,
    "biologie": 9.0
}
# Schrijf een functie calculate_average(grades: dict) -> float
# die het gemiddelde van alle punten berekent.

def calculate_average(grades: dict) -> float:
    totalnumber: float = 0.0
    totaltests: int  = 0.0
    for value in grades.values():
        totalnumber += value
        totaltests += 1
    return totalnumber / totaltests

print(calculate_average(grades))

# Opdracht 3:
nl_to_en = {
    "hond": "dog",
    "kat": "cat",
    "vis": "fish",
    "vogel": "bird"
}

# Schrijf een functie translate_to_english(text: str) -> str die een woord
# vertaalt naar het engels. Als het woord niet in de dict voorkomt,
# dan is de vertaling "Ik ken het woord niet"
# Los dit op met twee manieren:
#  - zonder een try except blok
#  - met een try except blok

def translate_to_english(text: str) -> str:
    notcorrect: str = "Ik ken het woord niet"
    for key in nl_to_en.keys():
        if key == text:
            return nl_to_en[key]
            break
    return notcorrect

print(translate_to_english("hond"))
print(translate_to_english("tijger"))

def translate_to_english2(text: str) -> str:
    try:
        return nl_to_en[text]
    except KeyError:
        return "Ik ken het woord niet"

print(translate_to_english2("hond"))
print(translate_to_english2("tijger"))

# opdracht 4:
# Je krijgt deze dict.
names_to_gender = {"Maggie":"F",
                   "Bart":"M",
                   "Homer":"M",
                   "Lisa": "F",
                   "Marge": "F"}
# Schrijf een function die telt hoeveel mannen en vrouwen er zijn.

def gender_counter(names: dict) -> (int, int):
    total_male: int = 0
    total_female: int = 0
    for value in names.values():
        if value == "M":
            total_male += 1
        elif value == "F":
            total_female += 1
    return total_male, total_female

print(gender_counter(names_to_gender))

# Opdracht 5:
# Transformeer names_to_gender naar gender_to_names
# Het resultaat is een dict van deze vorm:
# { "F": ["Lisa", "Marge", "Maggie"],
#  "M": ["Homer", "Bart" ]}
# De volgorde van de namen is niet belangrijk
# Hint: Maak een dict ret = {"F":[], "M":[]}
#       Overloop de items in names_to_gender
#       Als het M is, vraag ret["M"] op en voeg de naam toe
#       Als het F is, vraag ret["F"] op en voeg de naam toe

def gender_to_name(names: dict) -> dict:
    all_male: list = []
    all_female: list = []
    for key, value in names.items():
        if value == "M":
            all_male.append(key)
        elif value == "F":
            all_female.append(key)
    to_return: dict = {"F": all_female,
                       "M": all_male}
    return to_return

print(gender_to_name(names_to_gender))


# opdracht 6

# maak een lijst met 5 elementen
# vraag de gebruiker een getal (n)
# Haal print het n-de getal uit de lijst
# Zorg er voor da  het programma niet fout gaat als
# de gebruiker geen getal invoert, of n geen correcte index
# van de lijst is.

lst: list = [0, 1, 2, 3, 4]

def print_n(number_str: str):
    try:
        number = int(number_str)  # probeer te converteren naar int
        return lst[number]        # als index ongeldig is, gooit dit IndexError
    except ValueError:
        return "Dit is geen geldige waarde (geen getal)"
    except IndexError:
        return "Dit is geen geldige waarde (index buiten bereik)"

number = input("Geef een index in waarvoor je het nummer wil weten: ")
print(print_n(number))