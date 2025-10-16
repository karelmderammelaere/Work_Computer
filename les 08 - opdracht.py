#Het zijn veel oefeningen. Ontbreekt het je aan tijd?  Begin dan met 4 en 6.

# opdracht 1:
# Vraag de gebruiker om een bestandsnaam in te geven.
# Blijf vragen tot de gebruiker "Stop" ingeeft, of een bestandsnaam die bestaat.
# Zorg dat de code alle mogelijk errors opvangt.

def safe_open():
    while True:
        file_name = input("Enter text: (Stop stopt):")
        if file_name == "Stop":
            return print("This code has been stopped.")
        try:
            file = open(file_name, "r")  # opent file
            print("File opened successfully.")
            return file
        except FileNotFoundError:
            print(f"File {file_name} cannot be found.")
        except Exception as e:
            print(f"Something went wrong: {e}.")

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


data = []
def store_data():
    file = safe_open()
    if file is None:
        return
    for line in file:
        if line[-1] == "\n":
            line = line.replace("\n", "")
        name, sex, age = line.split(",")
        res = { "gender": sex, "age": age}
        data.append(res)
    print(data)


# opdracht 3:
# lees het bestand van opdracht 2 in (kies zelf: met of zonder header)
# schrijf de lijnen met mannen naar  bestandsnaam.m.txt
# schrijf de lijnen met vrouwen naar bestandsnaam.f.txt
# maak je code zo robuust mogelijk.

data_m = []
data_f = []
def seprate_m_f():
    print("\n Start separate M and F code \n")
    file = safe_open()
    file_m = open("C:\\Users\\0031803\\PycharmProjects\\PythonProject\\bestandsnaam.m.txt", "w")
    file_f = open("C:\\Users\\0031803\\PycharmProjects\\PythonProject\\bestandsnaam.f.txt", "w")
    if file is None:
        return
    for line in file:
        if line[-1] == "\n":
            line = line.replace("\n", "")
        name, sex, age = line.split(",")
        if sex == "M":
            file_m.write(line + '\n')
        elif sex == "F":
            file_f.write(line + '\n')
    file.close()
    file_m.close()
    file_f.close()
    return

print(seprate_m_f())

# opdracht 4: lees een python bestand in en tel het aantal lijnen die starten met een #

def count_comments():
    print("\n Start count comments code \n")
    total_comments: int = 0
    file = safe_open()
    if file is None:
        return
    for line in file:
        if line[0] == "#":
            total_comments += 1
    return total_comments

print(count_comments())

# opdracht 5: pas def safe_open(filename:str) uit 12_file.py ook werkt als het bestand bijvoorbeeld geopend is in MS-Word.

from docx import Document
print("python-docx werkt!")


def safe_open_rev(filename: str):
    try:
        # Voor Word-bestanden (.docx)
        if filename.lower().endswith(".docx"):
            doc = Document(filename)
            return doc
        # Voor tekstbestanden (.txt)
        elif filename.lower().endswith(".txt"):
            doc = open(filename, "r")
            return doc
        else:
            print("Onbekend bestandstype. Enkel .txt en .docx worden ondersteund.")
            return
    except FileNotFoundError:
        print(f"Bestand '{filename}' niet gevonden.")
        return
    except Exception as e:
        print(f"Fout bij openen of lezen van bestand: {e}")
        return

print(safe_open_rev("C:\\Users\\0031803\\PycharmProjects\\PythonProject\\Test document.docx"))


# opdracht 6: Neem de code in  12_file.py die het "Aantal aspirant developers extra sinds vandaag" telt.
#       - Pas aan dat lege lijn en lijnen met meer of minder dan 3 waardes, geen error geven bij split()
#       - Pas aan dat spaties voor een na de komma in het input bestaand worden weggewerkt

file = safe_open_rev("C:\\Users\\0031803\\PycharmProjects\\PythonProject\\testFile.txt")

if file is None:
    print("Bestand kon niet worden geopend.")

female_cnt = 0
student_cnt = 0
data = []

for line in file:
    line = line.strip()

    if line == "":
        continue
    parts = line.split(",")
    for i in range(len(parts)):
        parts[i] = parts[i].strip()
    if len(parts) != 3:
        print(f"Waarschuwing: regel heeft {len(parts)} waarden, wordt overgeslagen: {line}")
        continue

    name = parts[0]
    sex = parts[1]
    title = parts[2]

    if sex == "M":
        gender = "man"
    else:
        gender = "vrouw"
        female_cnt += 1


    if title == "Cursist":
        student_cnt += 1

    print(f"{name} is een {gender} en {title}")

    res = {"name": name, "gender": gender, "title": title}
    data.append(res)

print(data)