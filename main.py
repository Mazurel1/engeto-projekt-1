"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Jaroslav Hoferek
email: jaroslav.hoferek@seznam.cz
discord: Jaroslav H. Mazurel#7763
"""

from task_template import TEXTS

uvodni_text = "Dobrý den. Abyste mohl pokračovat do aplikace, \
musíte se napřed přihlásit."
oddelovac = "-" * 80
reg_uzivatele = {
    "bob": {"password": "123"},
    "ann": {"password": "pass123"},
    "mike": {"password": "password123"},
    "liz": {"password": "pass123"},
}

# Úvodní přivítání v aplikaci.

print(oddelovac)
print(uvodni_text.center(len(oddelovac)))
print(oddelovac)

# Vyžádání si přihlašovacích údajů od uživatele.

uziv_jmeno = input("Zadejte Vaše jméno: ")
uziv_heslo = input("Zadejte Vaše heslo: ")
print(oddelovac)

# Pokud je zadané jméno a heslo shodné s některým z registrovaných uživatelů,
#   pozdravit uživatele registrovaným jménem a zpřístupnit analyzování textu.
# Jinak ukončit program s upozorněním, že daný uživatel není zaregistrován.

print(oddelovac)
if uziv_jmeno in reg_uzivatele and uziv_heslo == reg_uzivatele[uziv_jmeno]["password"]:
    print(f"Ahoj {uziv_jmeno.capitalize()}. V aplikaci se nachází 3 texty k analýze.")
    
else:
    print("Nejste registrován nebo jste zadal špatně přihlašovací údaje")
    quit()

# Vybídnutí uživatele k výběru textu od 1 do 3.
# Pokud číslo neodpovídá číslu některého zadání
#   upozornit uživatele, že jeho výběr neodpovídá možným variantám a ukončit program.
# Jestli uživatel zadá neco jiného než číslo
#   upozornit uživatele, že zadal neplatná znak a ukončit program.
# Jinak použít hodnotu jako zvolenou variantu textu.

vyber_varianty = input("Zvolte variantu od 1 do 3: ")
print(oddelovac)

if str.isdigit(vyber_varianty) == False:
    print("Byl zadán neplatný znak.")
    quit()
elif int(vyber_varianty) < 1 or int(vyber_varianty) > 3:
    print("Vámi zvolená varianta nedodpovídá nabízeným možnostem.")
    quit()
else:
    varianta = TEXTS[(int(vyber_varianty) - 1)]

# Ocistení slov a výpis jejich počtu z analyzované varianty.
# Pro slovo v proměnné slova:
#   přidat hodnotu slovo, odříznout speciální znaky a převést na malé písmena
#   a přidat do listu vsechna_slova.
#   K proměnné pocet_slov přičíst +1.

vsechna_slova = []
pocet_slov = 0
slova = varianta.split()

for slovo in slova:
    vsechna_slova.append(slovo.strip(".,").lower())
    pocet_slov += 1

# Výpis slov začínajících velkým písmenem.
# Pro slovo ve varianta:
#   Pokud je na zacatku slova velke pismeno a 
#   přičtu k proměnné zacina_v_pismenem hodnotu +1.
#   Pokud je slovo psané celé velkýma písmenama,
#   připočtu k proměnné psane_v_pismenem +1.
#   Pokud je slovo psané celé malými písmeny,
#   připočtu k proměnné psane_m_pismeny +1
#   pokud je string číslo, připočtu k proměnné
#   string_je_cislo hodnotu +1, a slovo/hodnotu
#   zapíšu do seznamu cisla_v_textu.

zacina_v_pismenem = 0
psane_v_pismenem = 0
psane_m_pismeny = 0
string_je_cislo = 0
cisla_v_textu = []
soucet_cisel = 0

for slovo in varianta.split():
        if slovo[0].isupper():
            zacina_v_pismenem +=1
        elif slovo.isupper():
             psane_v_pismenem =+ 1
        elif slovo.islower():
             psane_m_pismeny += 1
        elif slovo.isnumeric():
             string_je_cislo += 1
             cisla_v_textu.append(slovo)
# Získání hodnoty součtu všech čísel v textu,
#   Pro číslo v cisla_v_textu, přičtu hodnotu jako integer 
#   k proměnné soucet_cisel.

for cislo in cisla_v_textu:
     soucet_cisel += int(cislo)

# Určení délky jednotlivých slov.
# Pro delka_slova v vsechna_slova:
#   proměnná pocet_znaku = 0
#       pokud je délka slova číslo,
#       Zapiš toto číslo do listu delky_slov.
#   Jinak:
#       Pro znaky v delka_slova:
#           za každý znak ve slovu, přičti
#           +1 do proměnné pocet_znaku a proměnnou
#           delka_znaku přidej do listu delky_slov.

delky_slov = []

for delka_slova in vsechna_slova:
    pocet_znaku = 0
    if len(delka_slova) == int:
         delky_slov.append(delka_slova)
    else:
         for znaky in delka_slova:
              pocet_znaku += 1
    delky_slov.append(pocet_znaku)

# Vytvoření slovníku, kdy klíčem je číslo
# znázorňující délku slova, a hodnoutou je 
# počet výskytů slova dané délky.
# Vytvořím slovník pocet_stejne_delky.
# pro delka v listu dely_slov:
#   v pocet_stejne_delky použít délku slova
#   jako hodnotu pro vytvoření položky ve slovníku
#   kde spočítej její výskyt a použíj jako její hodnotu.

pocet_stejne_delky = {}

for delka in delky_slov:
     pocet_stejne_delky[delka] = delky_slov.count(delka)

# Převedení slovníku pocet_stejne_delky na list.

delky_slov_list = list(pocet_stejne_delky.items())

print(f"V textu je {pocet_slov} slov.")
print(f"V textu je {zacina_v_pismenem} slov začínajicích velkým písmenem.")
print(f"V textu je {psane_v_pismenem} slov psaných velkými písmeny")
print(f"V textu je {psane_m_pismeny} slov psaných malými písmeny.")
print(f"V textu je {string_je_cislo} čísísel.")
print(f"Součet všech čísel v textu je {soucet_cisel}.")
print(oddelovac)

# Vytvoření grafu počtu opakování daného čísla.
# Pro delka a vyskyt v delky_slov_list:
#   proměnná stupníce je "*" znásoben výskyt.

print("Délka | Výskyt | Číslo")
print(oddelovac)

for delka, vyskyt in delky_slov_list:
     stupnice = vyskyt * "*"
     print(f"{delka:<3}| {stupnice:<17}| {vyskyt}")
print(oddelovac)
     
     
     


