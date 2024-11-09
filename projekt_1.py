"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zuzana Mogyorósi
email: zuzana.mogyorosi@gmail.com
discord: Zuzana M. - zuzanamogyorosi
"""

import task_template

uzivatelske_jmeno = input("Zadejte vaše uživatelské jméno: \n")
uzivatelske_heslo = input("Zadejte vaše heslo: \n")

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# Kontrola přihlášení
if uzivatelske_jmeno in registrovani_uzivatele:
    if registrovani_uzivatele[uzivatelske_jmeno] == uzivatelske_heslo:
        print(f"Vítejte {uzivatelske_jmeno}! Můžete analyzovat texty.")

        print("Vyberte jeden z následujících textů:")
        print("1: Text 1")
        print("2: Text 2")
        print("3: Text 3")
        
        vyber = input("Zadejte číslo textu (1-3): \n")
        
        if vyber == "1":
            vybrany_text = task_template.TEXTS[0]
        elif vyber == "2":
            vybrany_text = task_template.TEXTS[1]
        elif vyber == "3":
            vybrany_text = task_template.TEXTS[2]
        else:
            print("Neplatný výběr. Zkuste to znovu. \n")
            vybrany_text = None  

        if vybrany_text:
            print("Zvolený text k analýze: \n")
            print(vybrany_text)
            
            # analýza textu
            slova = vybrany_text.split()  # rozděli na seznam slov
            pocet_slov = len(slova)  # spočítá slova
            pocet_slov_velke_pismeno = sum(1 for slovo in slova if slovo[0].isupper()) # pokud jsou všechna písmena VELKÁ
            pocet_slov_velkymi_pismeny = sum(1 for slovo in slova if slovo.isupper()) # to samé
            pocet_slov_malymi_pismeny = sum(1 for slovo in slova if slovo.islower()) # pokud jsou všechna písmena malá
            
            # vyhledávání cisel 
            pocet_cisel = 0
            soucet_cisel = 0

            for slovo in slova:
                # najdi číselné části na začátku slova
                cislo_cast = ''
                for znak in slovo:
                    if znak.isdigit():
                        cislo_cast += znak
                    else:
                        break  # jak narazím na první nečíselný znak, přestane přidávat číslice
                if cislo_cast:  # jestli je nalezeno číslo na začátku slova
                    pocet_cisel += 1
                    soucet_cisel += int(cislo_cast)


            # Výpis výsledků
            print("Analýza textu: \n")
            print(f"Počet slov: {pocet_slov}")
            print(f"Počet slov začínajících velkým písmenem: {pocet_slov_velke_pismeno}")
            print(f"Počet slov psaných velkými písmeny: {pocet_slov_velkymi_pismeny}")
            print(f"Počet slov psaných malými písmeny: {pocet_slov_malymi_pismeny}")
            print(f"Počet čísel (včetně kombinací s textem): {pocet_cisel}")
            print(f"Součet všech čísel: {soucet_cisel}")
    else:
        print("Chybné heslo.")
else:
    print("Neregistrovaný uživatel.")
