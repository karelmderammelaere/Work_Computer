# opdracht 1:
# Vraag de gebruiker om een bestandsnaam in te geven.
# Blijf vragen tot de gebruiker "Stop" ingeeft, of een bestandsnaam die bestaat.
# Zorg dat de code alle mogelijk errors opvangt.

def print_n(file_name: str):
    try:
        number = int(number_str)  # probeer te converteren naar int
        return lst[number]        # als index ongeldig is, gooit dit IndexError
    except ValueError:
        return (f"Dit is geen correct bestand: {file_name}")
    except IndexError:
        return "Dit is geen geldige waarde (index buiten bereik)"

number = input("Geef een index in waarvoor je het nummer wil weten: ")
print(print_n(number))


# opdracht 2:
# Maak een bestand met deze inhoud:
"""
Naam,Geslacht,Leeftijd
Homer,M,36
Marge,F,34
Lisa,F,8
Bart,M,10
Maggie,F,1
"""

# Lees het bestand in.
# Lijn 1 bevat de kolomnamen en moet je negeren
# Maak een lijst van dicts "Name" -> (Sex, Age)

# opdracht 3:
# lees het bestand van opdracht 2 in (kies zelf: met of zonder header)
# schrijf de lijnen met mannen naar  bestandsnaam.m.txt
# schrijf de lijnen met vrouwen naar bestandsnaam.f.txt
# maak je code zo robuust mogelijk.

# opdracht 4: lees een python bestand in en tel het aantal lijnen ide starten met een #

# opdracht 5: pas def safe_open(filename:str) uit 12_file.py ook werkt als het bestand bijvoorbeeld geopend is in MS-Word.

# opdracht 6: Neem de code in  12_file.py die het "Aantal aspirant developers extra sinds vandaag" telt.
#       - Pas aan dat lege lijn en lijnen met meer of minder dan 3 waardes, geen error geven bij split()
#       - Pas aan dat spaties voor een na de komma in het input bestaand worden weggewerkt