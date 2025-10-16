def trouser_size(size: float):
    """
    Prints the name of a trouser size.
    :param size: Size of the trouser
    """
    if size < 40:
        return "Small"
    if size < 50:
        return "Medium"
    if size < 60:
        return "Large"
    if size < 70:
        return "XL"
    return "XXL"

# opdracht 1: schrijf code die test of trouser_size voor elke input de juiste output geeft.
#             beveilig de code tegen waardes die niet tussen 20 en 120 vallen.

test_cases = [
    (15, "not possible: out of range 20–120"),  # te klein
    (25, "Small"),
    (45, "Medium"),
    (55, "Large"),
    (65, "XL"),
    (85, "XXL"),
    (130, "not possible: out of range 20–120")  # te groot
]

for size, expected in test_cases:
    result = trouser_size(size)
    if result == expected:
        print(f"correct, size {size}: gives {result}")
    else:
        print(f"Test Failed, size {size}: gives '{result}', while '{expected}' expected")



# opdracht 1:
# Vraag de gebruiker om woorden in te geven ("Stop" stopt). Geef na elk woord feedback of het woord al eens gegeven is.

history =  set()

while True:
    word = input("Geef een woord:")
    if word == 'Stop':
        break
    if word in history:
        print("Woord is al gegeven")
    else:
        print("Woord is nog niet eerder gegeven")
        history.add(word)


# opdracht 2:
# Vraag de gebruiker om woorden in te geven ("Stop" stopt).
# Geef pas op het einde feedback of er dubbele woorden zijn ingegeven.
input_words =[]
unique_words = set()
while True:
    word = input("Geef een woord:")
    if word == 'Stop':
        break
    else:
        unique_words.add(word)
        input_words.append(word)
if len(unique_words) == len(input_words):
    print("All words are unique")
else:
    difference = len(input_words) - len(unique_words)
    print(f"You now have {difference} double word(s)")

# Je krijgt een dict die "Voornaam" mapt op "Familienaam".
dct={ "Arvid": "Claassen",
      "Nico" : "Van den Branden",
      "Patrick" : "Heirwegh",
      "Alexander": "Van den Branden",
      "Sofie": "Agten",
      "Karel": "De Rammelaere",
      "Arvid": "Van Tychem",
      "Homer": "Simpson"
      }

# opdracht 3: maak een set van alle familienamen
last_names = set(value for value in dct.values())
print(last_names)

# opdracht 4: Controleer of er een dubbele familienaam in zit: True/ False
correct = len(last_names) != len(dict(dct))
print(correct)

# opdracht 5: Maak een set met alle dubbele voornamen.
# type veranderen naar Lijst van tuples zodat we geen duplicates verliezen
pairs = [
    ("Arvid", "Claassen"),
    ("Nico", "Van den Branden"),
    ("Patrick", "Heirwegh"),
    ("Alexander", "Van den Branden"),
    ("Sofie", "Agten"),
    ("Karel", "De Rammelaere"),
    ("Arvid", "Van Tychem"),
    ("Homer", "Simpson")
]

first_names = [first for first, last in pairs]
duplicates = set(name for name in first_names if first_names.count(name) > 1)

print(duplicates)

print("sharing worked")
print("now for real")


