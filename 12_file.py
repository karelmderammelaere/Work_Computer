# python heeft ook een basis function om een bestand te lezen.
# file = open(filename, modus)
#    filename is de volledige path-name van het bestand.   C:\\documents\\tekst.txt
#    modus is wijze waarop het bestand geopend zal worden: "r" is leesmodus (read-only


my_file = "d:/dev/test.txt" # Wijzig naar een bestaand bestand

file = open(my_file,"r")

try :
    file = open(my_file[1],"r")
except FileNotFoundError:
    print("Bestand niet gevonden")

for line in file:
    print(line[:-1])

def safe_open(filename:str):
    try :
        file = open(filename,"r")
        return file
    except FileNotFoundError:
        print(f"Bestand '{filename}' niet gevonden")
        return None

# bouwen we langzaam code om onze eerst data analyze te komen:
# type mee

file = safe_open(my_file)
data = []
if file is None:
    exit()
female_cnt = student_cnt = 0
for line in file:
    print()
    print(line[:-1])
    line=line[:-1]
    parts = line.split(",")
    print(parts)
    name, sex, title = line.split(",")
    gender=""
    if sex == 'M':
        gender = "man"
    else:
        gender = "vrouw"
        female_cnt += 1
    if title == 'Cursist':
        student_cnt += 1
    print(f"{name} is een {gender} en {title}")
    res = { "name": name, "gender": gender, "title": title}
    data.append(res)
print(data)
print(f"Aantal vrouwen: {female_cnt}")
print(f"Aantal aspirant developers extra sinds vandaag: {student_cnt}")


#als we later pandas bestuderen zal bovenstaande lukken in een 5-tal lijnen


# python data wegschrijven
# open(filename, "w")
# maak een nieuw bestand / overschrijf bestaand
f = open(my_file,"w")  # pas op: my_file wordt overschreven
while True:
    text = input("Enter text: (Stop stopt):")
    if text == "Stop":
        break
    f.write(text + '\n')  # we moeten zelf de newline toevoegen
f.close()


python_group = [
    ['Karel', 'M', 'Cursist'],
    ['Begum', 'V', 'Cursist'],
    ['Sven', 'M', 'Cursist'],
    ['Alexander', 'M', 'Cursist'],
    ['Annaëlle', 'V', 'Cursist'],
    ['Christophe', 'M', 'Cursist'],
    ['Hamideh', 'V', 'Cursist'],
    ['Nico', 'M', 'Cursist'],
    ['Jean-Pierre', 'M', 'Cursist'],
    ['Olivier', 'M', 'Cursist'],
    ['Damiën', 'M', 'Cursist'],
    ['Patrick', 'M', 'Cursist'],
    ['Nina', 'V', 'Cursist'],
    ['Ellen', 'V', 'Cursist'],
    ['Arvid', 'M', 'Docent'],
    ['Raquel', 'V', 'Cursist'],
    ['Wesley', 'M', 'Cursist'],
    ['Sofie', 'V', 'Cursist']
]

f = open("d:/dev/persons.csv","w")
for person in python_group:
    f.write(",".join(person) + '\n')  # we moeten zelf de newline toevoegen
f.close()

# we hebben een csv-bestand gemaakt


f = open("d:/dev/persons.csv","r")
for line in f:  # somt alle lijnen één voor één op
    name, sex, type_ = line[:-1].split(",")
    print(f"{name} is een {type_}")
    if sex == 'V':
        print(f"{name} is een vrouw")
    else:
        print(f"{name} is een man")
f.close()


# Verschillende modes
# "r": lezen (tekst), fout als bestand niet bestaat
# "w": schrijven (tekst), truncate/maakt nieuw
# "a": toevoegen (tekst), schrijft aan einde

# "+": lees én schrijf (combineerbaar, bv. "r+", "w+", "a+")
# "r+": lezen/schrijven zonder trunceren
# "w+": lezen/schrijven met trunceren/aanmaken
# "a+": lezen en toevoegen; cursor op einde bij schrijven
# Als weet wat je aan het doen bent, dan kan je ook binaire bestanden inlezen of wegschrijven:
#   de modus wordt dan 'rb', 'wb' of 'ab'


# opdracht 1: lees een python bestand in en tel het aantal lijnen ide starten met een #
# opdracht 2: pas def safe_open(filename:str) uit 12_file.py ook werkt als het bestand bijvoorbeeld geopend is in MS-Word.
# opdracht 3: Neem de code in  12_file.py die het "Aantal aspirant developers extra sinds vandaag" telt.
#       - Pas aan dat lege lijn en lijnen met meer of minder dan 3 waardes, geen error geven bij split()
#       - Pas aan dat spaties voor een na de komma in het input bestaand worden weggewerkt



# read()	Reads the entire file as a string
# readline()	Reads one line at a time
# readlines()	Reads all lines into a list
# write()	Writes a string to the file
# writelines()	Writes a list of strings to the file
# close()	Closes the file
# flush()	Forces writing buffered data to disk
# seek(offset)	Moves the cursor to a specific byte position
# tell()	Returns the current cursor position
# truncate(size)	Cuts the file to a given size
# readable()	Returns True if the file can be read
# writable()	Returns True if the file can be written to

def  look_ahead(file, num: int =1) -> str:
    """
    Look ahead in a file for a specific number of characters
    :param file: file to look into
    :param num: number of characters to look ahead
    :return: string with the characters
    """
    pos = file.tell()  # save the current position
    peek = file.read(num) # read num bytes
    file.seek(pos) # return to the original position
    return peek
