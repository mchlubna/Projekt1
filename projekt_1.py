'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Chlubna
email: chlubnam@seznam.cz
"""
'''
TEXTS = ['''                                    
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#slovnik uzivatel - password
users_pwd = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123",}

#rozdeleni textu
count_texts = len(TEXTS)

#definice oddelovace pro print
oddelovac = "-" * 60

#zadani uzivatele
jmeno = input("Zadej jmeno: ")
pwd = input("Zadej password: ") 



#overeni uzivatele
if jmeno in users_pwd.keys() and pwd == users_pwd.get(jmeno, pwd):
    print(oddelovac,f"Welcome to the app, {jmeno}",f"We have {count_texts} texts to be analyzed.",oddelovac,sep = "\n")
    
    #vyber textu pro anylyzu
    text_choice = input(f"Enter a number btw. 1 and {count_texts} to select: ")
    print(oddelovac)
    if int(text_choice) <= count_texts:
        #nastaveni textu pro analyzu
        text_to_analyze = TEXTS[int(text_choice)-1]
        
        #definice promennych
        text_slova = []
        vyskyt = {}
        zacatek_velke_pismeno = 0
        vse_velke = 0
        vse_male = 0
        cisla_pocet = 0
        cisla_sum = 0 

        #vytvoreni seznamu vycistenych slov       
        for slovo in text_to_analyze.split(" "):
            if "\n" in slovo:
                rozdelena_slova = slovo.split("\n")
                if len(rozdelena_slova[0]):
                        text_slova.append(rozdelena_slova[0].strip(".,"))
                if len(rozdelena_slova[1]):
                        text_slova.append(rozdelena_slova[1].strip(".,"))
            elif len(slovo):
                text_slova.append(slovo.strip(".,"))

        #analyza slov
        for slovo in text_slova:
            #print(slovo[0])
            if slovo[0].isupper() and not slovo.isupper():
                zacatek_velke_pismeno = zacatek_velke_pismeno + 1
            if slovo.islower():
                vse_male = vse_male + 1
            if slovo.isupper():
                vse_velke = vse_velke + 1
            if slovo.isdigit():
                cisla_pocet = cisla_pocet + 1
                cisla_sum = cisla_sum + int(slovo)
            if len(slovo) in vyskyt.keys():
                vyskyt[len(slovo)] = vyskyt[len(slovo)]+1
            else:
                 vyskyt[len(slovo)] = 1
        
        #seřazení vytvoreneho slovniku podle klicu      
        vyskyt = dict(sorted(vyskyt.items()))  

        #print vystupu
        print(f"There are {len(text_slova)} words in the selected text.")
        print(f"There are {zacatek_velke_pismeno} titlecase words.")
        print(f"There are {vse_velke} uppercase words.")
        print(f"There are {vse_male} lowercase words.")
        print(f"There are {cisla_pocet} numeric strings.")
        print(f"The sum of all the numbers {cisla_sum}")
        maximalni_vyskyt = max(vyskyt.values())
        print(oddelovac)
        print("LEN|".rjust(4),"OCCURENCES".center(maximalni_vyskyt+1),"|NR.")
        print(oddelovac)
        for delka, vyskyty in vyskyt.items():
            print(str(delka).rjust(3),"|","*" * vyskyty,"|".rjust(maximalni_vyskyt-vyskyty+4), vyskyty, sep = "")

        #vybrany text jiny nez v nabidce
    else: print("Vyber neni k dispozici")
#user name doesn't exist or pwd is wrong
else:
    print(f"User name {jmeno} doesn't exist or {pwd} is wrong password")