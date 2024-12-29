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
north of US 30N and the Union Pacific Railroad,
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
prvni_text = TEXTS[0]
druhy_text = TEXTS[1]
treti_text = TEXTS[2]

#definice oddelovace pro print
oddelovac = "-" * 60

#zadani uzivatele
jmeno = input("Zadej jmeno: ")
pwd = input("Zadej password: ") 

#overeni uzivatele
if jmeno in users_pwd.keys() and pwd == users_pwd.get(jmeno, pwd):
    print(oddelovac,f"Welcome to the app, {jmeno}","We have 3 texts to be analyzed.",oddelovac,sep = "\n")
    
    #vyber textu pro anylyzu
    text_choice = input("Enter a number btw. 1 and 3 to select: ")
    print(oddelovac)
  
    if text_choice in ("1","2","3"):
     #nastaveni textu pro analyzu
        if text_choice == "1":
         text_to_analyze = prvni_text
        elif text_choice == "2":
         text_to_analyze = druhy_text
        elif text_choice =="3":
         text_to_analyze = treti_text
    
        #definice promennych
        text_slova = []
        vyskyt = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}
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
            if slovo[0].isupper():
                zacatek_velke_pismeno = zacatek_velke_pismeno + 1
            if slovo.islower():
                vse_male = vse_male + 1
            if slovo.isupper() and not any(char.isdigit() for char in slovo):
                vse_velke = vse_velke + 1
            if slovo.isdigit():
                cisla_pocet = cisla_pocet + 1
                cisla_sum = cisla_sum + int(slovo)
            if len(slovo) == 1:
                vyskyt[1] = vyskyt[1]+1
            elif len(slovo) == 2:
                vyskyt[2] = vyskyt[2]+1
            elif len(slovo) == 3:
                vyskyt[3] = vyskyt[3]+1
            elif len(slovo) == 4:
                vyskyt[4] = vyskyt[4]+1  
            elif len(slovo) == 5:
                vyskyt[5] = vyskyt[5]+1 
            elif len(slovo) == 6:
                vyskyt[6] = vyskyt[6]+1
            elif len(slovo) == 7:
                vyskyt[7] = vyskyt[7]+1
            elif len(slovo) == 8:
                vyskyt[8] = vyskyt[8]+1
            elif len(slovo) == 9:
                vyskyt[9] = vyskyt[9]+1  
            elif len(slovo) == 10:
                vyskyt[10] = vyskyt[10]+1
            elif len(slovo) == 11:
                vyskyt[11] = vyskyt[11]+1            
                          
        print(vyskyt)
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
#user name doesn't exist or wrong pwd
else:
    print(f"User name {jmeno} doesn't exist or {pwd} is wrong password")





