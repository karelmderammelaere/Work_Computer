my_set = set()
check_set = set()

while True:
    word = input("Give a word, if Stop stops: ")
    if word == "Stop":
        break
    check_set.add(word)
    if len(check_set) == len(my_set):
        print("This word is already in this set")
    #other option see below
    #elif word in word_set:
    #   print(f"{word} is already given")
    else:
        my_set.add(word)


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

#print alle dames in python_group
for item in python_group:
    if item[1] == "V":
        print(item[0])

#maak lijst met alle heren in python group
list_m = []
for item in python_group:
    if item[1] == "M":
        list_m.append(item[0])
print(list_m)

#tel het aantal dames in python group
count_f = 0
for item in python_group:
    if item[1] == "V":
        count_f += 1
print(count_f)


#optie 2
count_f2 = 0
for name, sex, type in python_group:
    if sex == "V":
        count_f2 += 1
print(count_f2)

