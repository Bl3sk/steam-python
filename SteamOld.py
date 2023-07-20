import linecache
import random
import time
import os

from game import *
import grid as gr
global ztraceno, chyceno


seznam_her = ["eggCatcher", "guessNumber"]

def uvod():
    seznam_menu = ["1 Registrace", "2 Přihlásit se"]
    print("Nemáte ještě učet? Zaregistrujte se!")
    for polozka in seznam_menu:
        print(polozka)
    print("Vyberte možnost z menu 1-"+str(len(seznam_menu)))
    menu_odpoved = input()
    if menu_odpoved == "1":
        registrovat()
    elif menu_odpoved == "2":
        prihlasit()
    else:
        print("\nZadali jste piovinu!")
        uvod()

def vytvorSlozku(uzivatel_nazev):
    try:
        if not os.path.exists(uzivatel_nazev):
            os.makedirs(uzivatel_nazev)
    except OSError:
        print ('Error: Creating uzivatel_nazev. ' +  uzivatel_nazev)
    time.sleep(1)    
    for hra in seznam_her:
        current = os.getcwd()
        slozka = "\\"+uzivatel_nazev
        save_path = current+slozka
        file_name = ""+hra+".txt"
        completeName = os.path.join(save_path, file_name)
        #print(completeName)
        myfile = open(completeName, "w")
        myfile.write("noDataYet")
        myfile.close()

def zapis_data_GuessNumber(pocet):
    global prihlaseny_uzivatel
    #print("Připsat", pocet, prihlaseny_uzivatel)
    current = os.getcwd()
    slozka = "\\"+prihlaseny_uzivatel
    save_path = current+slozka
    file_name = "guessNumber.txt"
    completeName = os.path.join(save_path, file_name)
    #print(completeName)
    myfile = open(completeName, "r+")
    obsah = myfile.read()
    if obsah == "noDataYet" or int(obsah) > pocet:
        print("Gratulujeme! Váš osobní rekord!")
        myfile.seek(0)
        myfile.write(str(pocet))
        myfile.truncate()
    else:
        print("Váš osobní rekord je: "+obsah+" pokusů.")
    #myfile.write("pocet")
    myfile.close()
    #print("hotovo")
    guessNumber()


def registrovat():
    file_name = open("uzivatele.txt")
    uzivatele_seznam = file_name.readlines()
    file_name.close()
    
    print(uzivatele_seznam)
    print("\nZadejte uživatelské jméno, pod kterým se budete přihlašovat:\n")
    global registrace_odpoved
    registrace_odpoved = input()
    if registrace_odpoved+"\n" in uzivatele_seznam:
        print("Uživatelské jméno je již zabrané. Zvolte jiné.")
        registrovat()
    else:
        with open("uzivatele.txt", "a") as uzivatel:
            uzivatel.write(registrace_odpoved+"\n") 
    print("\nRegistrace proběhla úspěšně.\n")
    vytvorSlozku('./'+registrace_odpoved+'/')
    prihlasit()
 
def prihlasit():
    global prihlaseny_uzivatel
    uzivatele = []
    f = open('uzivatele.txt','r')
    for line in f:
        uzivatele.append(line.strip())
    print("\nPro přihlášení zadejte své uživatelské jméno na steamu:\n")
    jmeno = input()
    if jmeno in uzivatele:
        print("\nVítej "+jmeno+"! Příhlášení proběhlo v pořádku.\n")
        prihlaseny_uzivatel = jmeno
    else:   
        print("\nNesprávné uživatelské jméno! Před přihlášením se zaregistrujte.\n")
        uvod()

def odhlasit():
    print("Byl jste úspěšně odhlášen.")
    print("")
    prihlasit()

def loading(hra):
    print("Načítání "+hra+"...")
    time.sleep(1)
    print("Načítání "+hra+"...10%")
    time.sleep(1)
    print("Načítání "+hra+"...65%")
    time.sleep(1)
    result = eval(hra + "()")
    print(result)
    
def guessNumber_normal():
    obtiznosti_list = ["1 Snadné(1-100)", "2 Akorát(1-1000)", "3 Expert(1-10000)"]
    print("\nZvolte obtížnost:")
    for polozka in obtiznosti_list:
        print(polozka)
    print("Vyberte možnost z menu 1-"+str(len(obtiznosti_list)))
    odpoved = input()
    if odpoved == "1":
        rozmezi = "1-100"
        cislo = random.randint(1, 100)
    elif odpoved == "2":
        rozmezi = "1-1000"
        cislo = random.randint(1,1000)
    elif odpoved == "3":
        rozmezi = "1-10000"
        cislo = random.randint(1,10000)
    else:
        print("Zadali jste piovinu!")
        guessNumber()
    print("Zadejte svůj tip " +rozmezi+":")
    pocet = 0
    while True:
        pocet += 1
        tip = input()
        if int(tip) == cislo:
            print("Gratulujeme! Uhodli jste číslo!")
            print("Stačilo vám k tomu "+str(pocet)+" pokusů.")
            False
            guessNumber()
        elif int(tip) > cislo:
            print("Tipli jste moc vysoko. :(")
        elif int(tip) < cislo:
            print("Tipli jste moc nízko. :(")
    
def guessNumber_ranked():
    rozmezi = "1-1000"
    cislo = random.randint(1,10)
    print("Zadejte svůj tip " +rozmezi+":")
    pocet = 0 
    while True:
        pocet += 1
        tip = input()
        if int(tip) == cislo:
            print("Gratulujeme! Uhodli jste číslo!")
            print("Stačilo vám k tomu "+str(pocet)+" pokusů.")
            zapis_data_GuessNumber(pocet)
            False
        elif int(tip) > cislo:
            print("Tipli jste moc vysoko. :(")
        elif int(tip) < cislo:
            print("Tipli jste moc nízko. :(")
    
   
       
def guessNumber():
    seznam_menu = ["1 Cvičné", "2 Ranked", "3 Zpět na Plochu"]
    print("\nZvolte obtížnost:")
    for polozka in seznam_menu:
        print(polozka)
    print("Vyberte možnost z menu 1-"+str(len(seznam_menu)))
    odpoved = input()
    if odpoved == "1":
        guessNumber_normal()
    elif odpoved == "2":
        guessNumber_ranked()
    elif odpoved == "3":
        knihovna()
    else:
        print("\nZadali jste piovinu!")
    
def reactTime():
    pass    


def eggCatcher():
    print("Pohybujte se klávesami A - doleva   D - doprava  a posbírejte co nejvíc vájet na amoletu!! To bude mňamina!")
    time.sleep(5)
    game_loop()
    print(gr.chyceno, gr.ztraceno)
    time.sleep(5)

def knihovna():
    seznam_menu = ["1 GuessNumber", "2 EggCatcher", "3 Menu"]
    for polozka in seznam_menu:
        print(polozka)
    print("\nVyberte možnost z menu 1-"+str(len(seznam_menu)))
    menu_odpoved = input()
      
    if menu_odpoved == "1":
        loading("guessNumber")
    elif menu_odpoved == "2":
        loading("eggCatcher")
    elif menu_odpoved == "3":
        vyber()
    else:
        print("\nZadali jste piovinu!")
        knihovna()
        
def obchod():
    print("\nJe nám líto, ale tato položka je stále ve vývoji.")
    vyber()

def ukoncit():
    print("")
    exit()

def vyber():
    seznam_menu = ["1 Obchod","2 Knihovna her", "3 Odhlásit", "4 Ukončit"]
    for polozka in seznam_menu:
        print(polozka)
    print("\nVyberte možnost z menu 1-"+str(len(seznam_menu)))
    menu_odpoved = input()
    
    options = {1 : obchod,
           2 : knihovna,
           3 : odhlasit,
           4 : ukoncit,
}   
    try:
        options[int(menu_odpoved)]()
    except:
        print("\nZadali jste piovinu!")
        vyber()
       
uvod()
while True:
    vyber()