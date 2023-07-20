import linecache
import random
import time
import os
import bcrypt
import pandas as pd
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt
from art import * 
import matplotlib.pyplot as plt

from game import *
import grid as gr
from obrazky import *

class MenuFunkce():
    def over_heslo(self, heslo):
            if heslo == "nudavpraci":
                clearConsole()
                tprint("Steam",font="block",chr_ignore=True)
                menu.uvod()
            else:
                clearConsole()
                tprint("Security")
                print("Byl zadán nesprávný přístupový údaj.\nBudete vykázáni za:")
                x = 5
                while x > 0:
                    print(".... ",x)
                    time.sleep(1);x-=1 
                exit()
                
    def over_odpoved(self, odpoved, rozmezi):
        if odpoved.isdigit() == False or int(odpoved) > rozmezi or int(odpoved) < 0:
            print("\nZadali jste hodnotu mimo rozsah!\n")
            return False
        else:
            return True
            
    def zmen_barvu(self):
        seznam_barev = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
        rnd1 = random.randint(1, len(seznam_barev)-1)
        rnd2 = random.randint(1, len(seznam_barev)-1)
        os.system("color "+str(seznam_barev[rnd1]) + str(seznam_barev[rnd2])+"")
        menu.obchod()
        
    def zadani_hesla(self, uzivatel_odpoved):
        db = Databaze()
        print("\nZvolte si heslo(3-8 znaků):\n")
        heslo_odpoved = input()
        if len(heslo_odpoved) < 3 or len(heslo_odpoved) > 8:
            print("Nesplnili jste správný formát hesla!")
            menu.uvod()
        else:
            print("Pro ověření správnosti hesla, zadejte heslo znovu:")
            heslo_znovu = input()
            if heslo_odpoved == heslo_znovu:
                db.pridej_uzivatele(uzivatel_odpoved, heslo_odpoved)
                print("\nRegistrace proběhla úspěšně.\n")
                menu.uvod()
            else:
                print("Hesla se neshodují, zkuste to znovu.")
                menu.uvod()
                
    def zobraz_menu(self, seznam_menu):
        slovnik_menu = {}
        slovnik_funkci = {
            "Hlavní menu" : menu.hlavni_menu,
            "Profil" : menu.profil,
            "Obchod" : menu.obchod,
            "Knihovna her" : menu.knihovna,
            "Síň slávy" : menu.sin_slavy,
            "Diskuze" : menu.diskuze,
            "Přihlášení" : menu.prihlasit,
            "Registrace" : menu.registrovat,
            "Odhlásit" : menu.odhlasit,
            "Ukončit" : exit,
            "Mystery skin na GUI" : menufun.zmen_barvu,
            "EggCatcher" : hry.eggCatcher,
            "GuessNumber" : hry.guessNumber,
            "SpeedyCalc" : hry.speedyCalc,
            "TypeRace" : hry.typeRace,
            "Ňufící vs Zombies [¬º-°]¬" : hry.nuficivsZombies,
            "Hrát kompetitivní hru" : hry.nic,
            "Ukončit hru" : menu.knihovna
        }
        for hodnota in range(len(seznam_menu)):
            slovnik_menu[hodnota+1] = seznam_menu[hodnota]
            print('%s %s' % (hodnota+1 , seznam_menu[hodnota]))
        menu_odpoved = input("Vyberte možnost z menu 1-"+str(len(seznam_menu))+": ")
        if menu_odpoved.isdigit() == False or int(menu_odpoved) > len(seznam_menu) or int(menu_odpoved) < 0:
            print("\nZadali jste hodnotu mimo rozsah!\n")
            return False
        else:
            return slovnik_funkci[slovnik_menu[int(menu_odpoved)]]
            
class MenuSeznam():
    def __init__(self):
        self.prihlaseny_uzivatel = ""
        
    def povoleni_vstup(self):
        tprint("Panasonic")
        odpoved_heslo = input("Upozornění: Při zadání nesprávného přístupového údaje budete násilím vykázáni!\nZadejte přístupový údaj:")
        menufun.over_heslo(odpoved_heslo)  
    
    def uvod(self):
        print("Nemáte ještě učet? Zaregistrujte se!")
        volani = menufun.zobraz_menu(["Registrace", "Přihlášení", "Ukončit"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            self.uvod()
        else:
            volani()
                          
    def registrovat(self):
        print("\nZadejte uživatelské jméno, pod kterým se budete přihlašovat:\n")
        uzivatel_odpoved = input()
        if db.prazdna_db() == False:
            if db.uzivatel_exist(uzivatel_odpoved) == True:
                print("Uživatelské jméno je již zabrané. Zvolte jiné.")
                self.registrovat()
            else:
                menufun.zadani_hesla(uzivatel_odpoved)
        else:
            menufun.zadani_hesla(uzivatel_odpoved)
            
    def prihlasit(self):
        login_jmeno = input("\nZadejte své uživatelské jméno:")
        login_heslo = input("Zadejte heslo ke svému účtu:")
        if db.over_prihlaseni(login_jmeno, login_heslo) == True:
            self.prihlaseny_uzivatel = login_jmeno
            print("\nVítej "+self.prihlaseny_uzivatel+"! Příhlášení proběhlo v pořádku.\n")
            clearConsole()
            self.hlavni_menu()
        else:
            print("\nZadali jste nespravné uživatelské jméno nebo heslo.\n")
            self.uvod()
            
    def odhlasit(self):
        print("\nByl jste úspěšně odhlášen.\n")
        self.uvod() 
        
    def hlavni_menu(self):
        clearConsole()
        tprint("MENU")
        print(self.prihlaseny_uzivatel)
        volani = menufun.zobraz_menu(["Profil", "Obchod", "Knihovna her", "Síň slávy", "Diskuze", "Odhlásit", "Ukončit"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            self.hlavni_menu()
        else:
            volani()

    def obchod(self):
        clearConsole()
        tprint("Obchod")
        volani = menufun.zobraz_menu(["Mystery skin na GUI", "Hlavní menu"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            self.obchod()
        else:
            pass
            volani()
        
    def knihovna(self):
        clearConsole()
        tprint("Knihovna")
        volani = menufun.zobraz_menu(["EggCatcher", "GuessNumber", "SpeedyCalc", "TypeRace", "Ňufící vs Zombies [¬º-°]¬", "Hlavní menu"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            self.knihovna()
        else:       
            volani()
        
    def profil(self):
        clearConsole()
        tprint(self.prihlaseny_uzivatel)
        print("Datum registrace: ",db.ziskej_data("Registrace"))
        print("Rekord EggCatcher: ",db.ziskej_data("EggCatcher"),"%")
        print("Rekord GuessNumber: ",db.ziskej_data("GuessNumber"))
        print("Rekord SpeedyCalc: ",db.ziskej_data("SpeedyCalc"))
        print("Rekord TypeRace: ",db.ziskej_data("TypeRace"),"s")
        print("Rekord Ňufící vs Zombies: ",db.ziskej_data("NuficivsZombies"), "\n")
        volani = menufun.zobraz_menu(["Hlavní menu"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            self.profil()
        else:       
            volani()
     
    def sin_slavy(self):
        clearConsole()
        seznam_her = ("EggCatcher", "GuessNumber", "SpeedyCalc", "TypeRace", "NuficivsZombies")
        tprint("TOP SKORE")
        print("Níže můžete vidět nejlepší výsledky TOP 5 hráčů dané hry.\n")
        for hra in seznam_her:
            print("\n",hra)
            print(db.zobraz_zebricek(hra).to_string())
        print("")
        volani = menufun.zobraz_menu(["Profil", "Hlavní menu"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            self.sin_slavy()
        else:       
            volani()
             
    def diskuze(self):
        clearConsole()
        tprint("Diskuze")
        while True:
            print("Limit: zpráva/5s, zpráva/30 znaků . Pro opuštění diskuze zadejte příkaz !konec \n")
            print(db.zobraz_diskuzi())
            zprava = input("Napište zprávu: ")
            if zprava == "!konec":
                self.hlavni_menu()
            elif len(zprava) > 30:
                print("Překročili jste limit zprávy 30 znaků.")
            else:
                db.aktualizuj_diskuzi(zprava)
                time.sleep(1)
                self.diskuze()                      
    
class Databaze():
    uziv_data = "data.csv"
    dis_data = "diskuze.csv"
    def uzivatel_exist(self, uzivatel):
        df = pd.read_csv(self.uziv_data)
        return uzivatel in df['Uzivatel'].unique()
    def prazdna_db(self):
        df = pd.read_csv(self.uziv_data)
        if df.shape[0] == 0:
            return True 
        else:
            return False
    def over_prihlaseni(self, uzivatel, heslo):
        passwd = bytes(heslo, encoding="utf-8")
        df = pd.read_csv(self.uziv_data)
        df_filtr = df.set_index("Uzivatel", drop=False)
        try:
            db_heslo = df_filtr.loc[uzivatel]['Heslo']
        except:
            return False
        if uzivatel not in df['Uzivatel'].values:
            return False
        else:
            if bcrypt.checkpw(passwd, bytes(db_heslo, encoding="utf-8")):
                return True
            else:
                return False
                
    def pridej_uzivatele(self, uzivatel, heslo):
        df = pd.read_csv(self.uziv_data)
        datum = date.today()
        hsh_heslo = bytes(heslo, encoding="utf-8")
        salt = bcrypt.gensalt()
        hsh_heslo = bcrypt.hashpw(hsh_heslo, salt)
        novy_zaznam = {'Uzivatel':uzivatel,'Heslo': hsh_heslo.decode('utf-8'),'Registrace': datum.isoformat(),'EggCatcher':'Nan','GuessNumber':'Nan', 'SpeedyCalc':'Nan', 'TypeRace':'Nan', 'NuficivsZombies':'Nan'}
        df = df.append(novy_zaznam, ignore_index=True)
        df.to_csv(self.uziv_data, index=False)
    
    def ziskej_data(self, sloupec):
        df = pd.read_csv(self.uziv_data)
        df_filtr = df.set_index("Uzivatel", drop=False)
        df_filtr = df.set_index("Uzivatel", drop=False)
        return df_filtr.loc[menu.prihlaseny_uzivatel][sloupec]
        
    def aktualizuj_data(self, hodnota, sloupec):
        df = pd.read_csv(self.uziv_data)
        ind = df.index[df["Uzivatel"]==menu.prihlaseny_uzivatel].tolist()      
        df.at[ind,sloupec] = hodnota
        df.to_csv(self.uziv_data, index=False)
        
    def zobraz_diskuzi(self):
        df = pd.read_csv(self.dis_data)
        df = df.to_string(index=False)
        return df
        
    def aktualizuj_diskuzi(self, text):
        df = pd.read_csv(self.dis_data)
        now = datetime.now()
        aktualni_cas = now.strftime("%H:%M")
        datum = date.today()
        novy_zaznam = {'Uzivatel':menu.prihlaseny_uzivatel, 'Datum': datum.isoformat(), 'Cas': aktualni_cas, 'Zprava': text}
        df = df.append(novy_zaznam, ignore_index=True)
        df.to_csv(self.dis_data, index=False)
        if len(df.index) > 15:
            df = df.reset_index(drop=True)
            df = df.drop([0, 0])
            df.to_csv(self.dis_data, index=False)
           
    def zobraz_zebricek(self, hra):
        slovnik_hodnot = {"EggCatcher" : ["Úspěšnost", False], "GuessNumber" : ["Počet pokusů", True], "SpeedyCalc" : ["Vypočtených příkladů", False], "TypeRace" : ["Čas[s]", True], "NuficivsZombies" : ["Skore", False]}
        hod = slovnik_hodnot[hra]
        df = pd.read_csv(self.uziv_data)
        df = df[df[hra] != "Nan"]
        df[hra] = pd.to_numeric(df[hra])
        df = df.sort_values(by=[hra], ascending=hod[1]).reset_index(drop=True).head(5)
        df.index = df.index + 1 
        zmena_df = df.rename(columns={"Uzivatel": "Hráč",hra: hod[0]})
        zmena_df = zmena_df[["Hráč", hod[0]]]
        return zmena_df
        
    def zobraz_graf(self, hra, vysledek):
        slovnik_hodnot = {"EggCatcher" : ["Úspěšnost", False], "GuessNumber" : ["Počet pokusů", True], "SpeedyCalc" : ["Vypočtených příkladů", False], "TypeRace" : ["Čas[s]", True], "NuficivsZombies" : ["Skore", False]}
        hod = slovnik_hodnot[hra]
        df = pd.read_csv(self.uziv_data)
        df = df[df[hra] != "Nan"]
        df[hra] = pd.to_numeric(df[hra])
        df = df.sort_values(by=[hra], ascending=hod[1]).reset_index(drop=True).head(5)
        hraci = df['Uzivatel'].tolist()
        hraci.insert(0, "Poslední výsledek")
        hraci = ["Váš rekord" if x== menu.prihlaseny_uzivatel else x for x in hraci]
        vysledky = df[hra].tolist()
        vysledky.insert(0, vysledek)
        barlist=plt.bar(hraci, vysledky)
        barlist[0].set_color('r')
        plt.xlabel('Hráč')
        plt.ylabel('Výsledek')
        plt.title('Tvé výsledky v porovnání s výsledky ostatních hráčů')
        plt.show()


class Hry():
    def loading(self, hra):
            clearConsole()
            print("Načítání "+hra+"...")
            time.sleep(0.5)
            print("Načítání "+hra+"...10%")
            time.sleep(0.5)
            print("Načítání "+hra+"...65%")
            time.sleep(0.5)
            print("Načítání "+hra+"...100%")

    def nic(self):
        pass
    
    def eggCatcher(self):
        volani = menufun.zobraz_menu(["Hrát kompetitivní hru", "Ukončit hru"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            self.eggCatcher()
        else:       
            volani()
        self.loading("eggCatcher")
        tprint("EggCatcher")
        print("Pohybujte se klávesami A - doleva   D - doprava  a posbírejte co nejvíc vajec na amoletu!! To bude mňamina!")
        time.sleep(3)
        game_loop()
        pred_vysledek = db.ziskej_data("EggCatcher")
        uspesnost = round(100 * gr.chyceno/(gr.ztraceno+gr.chyceno), 2)
        print("Chytil jsi "+str(uspesnost)+"% vajec.")
        if  pred_vysledek == "Nan" or float(pred_vysledek) < uspesnost:
            print("Gratulujeme! Váš osobní rekord!")
            db.aktualizuj_data(uspesnost, "EggCatcher")            
        else:
            print("Váš osobní rekord je: "+str(pred_vysledek)+" pokusů.")
        db.zobraz_graf("EggCatcher", uspesnost)
        input("Stisknutím klávesy Enter se vrátite do menu.")
        self.eggCatcher()
        
    def guessNumber_normal(self):
        obtiznosti_list = ["1 Snadné(1-100)", "2 Akorát(1-1000)", "3 Expert(1-10000)"]
        print("\nZvolte obtížnost:")
        for polozka in obtiznosti_list:
            print(polozka)
        odpoved = input("Vyberte možnost z menu 1-"+str(len(obtiznosti_list)))
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
            self.guessNumber()
        print("Zadejte svůj tip " +rozmezi+":")
        pocet = 0
        while True:
            pocet += 1
            tip = input()
            if int(tip) == cislo:
                print("Gratulujeme! Uhodli jste číslo!")
                print("Stačilo vám k tomu "+str(pocet)+" pokusů.")
                break
            elif int(tip) > cislo:
                print("Tipli jste moc vysoko. :(")
            elif int(tip) < cislo:
                print("Tipli jste moc nízko. :(")
        input("Stisknutím klávesy Enter se vrátite do menu.")
        self.guessNumber()
        
    def guessNumber_ranked(self):
        rozmezi = "1-1000"
        cislo = random.randint(1,1000)
        print("Zadejte svůj tip " +rozmezi+":")
        pocet = 0 
        while True:
            pocet += 1
            tip = input()
            if int(tip) == cislo:
                print("Gratulujeme! Uhodli jste číslo!")
                print("Stačilo vám k tomu "+str(pocet)+" pokusů.")
                break
            elif int(tip) > cislo:
                print("Tipli jste moc vysoko. :(")
            elif int(tip) < cislo:
                print("Tipli jste moc nízko. :(")
        print(db.ziskej_data("GuessNumber"))
        pred_vysledek = db.ziskej_data("GuessNumber")
        if  pred_vysledek == "Nan" or int(pred_vysledek) > pocet:
            print("Gratulujeme! Váš osobní rekord!")
            db.aktualizuj_data(pocet, "GuessNumber")            
        else:
            print("Váš osobní rekord je: "+pred_vysledek+" pokusů.")
        db.zobraz_graf("GuessNumber", pocet)
        input("Stisknutím klávesy Enter se vrátite do menu.")
        self.guessNumber()  
        
    def guessNumber(self):
        clearConsole()
        self.loading("GuessNumber")
        tprint("GuessNumber")
        seznam_menu = ["1 Cvičné", "2 Kompetitivní", "3 Ukončit hru"]
        for polozka in seznam_menu:
            print(polozka)
            moznosti = {1 : self.guessNumber_normal,
                   2 : self.guessNumber_ranked,
                   3 : menu.knihovna,
                             }  
        menu_odpoved = input("Vyberte možnost z menu 1-"+str(len(seznam_menu))+"\n")
        if menufun.over_odpoved(menu_odpoved, len(seznam_menu)) == True:
            pass
        else:
            menu.knihovna()
        moznosti[int(menu_odpoved)]()
        
    def speedyCalc(self):
        clearConsole()
        self.loading("SpeedyCalc")
        tprint("SpeedyCalc")
        volani = menufun.zobraz_menu(["Hrát kompetitivní hru", "Ukončit hru"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            time.sleep(1)
            self.hlavni_menu()
        else:
            volani()
        ops = {"+": (lambda a,b: a+b), "-": (lambda a,b: a-b)}
        pocet_spravne = 0
        start = time.time()
        konec = 0
        while int(konec - start) < 15:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            op = random.choice(["+", "-"])
            odpoved = input("%s %s %s = "%(a,op,b,))
            vysledek = ops[op] (a, b)
            if odpoved.lstrip('-').isdigit() == False:
                print("Zadávejte pouze čísla.")
            elif int(odpoved) == int(vysledek):
                print("Správně")
                pocet_spravne += 1
            else:
                print("Špatně. Správný výsledek je: ",vysledek)
            konec = time.time()
        print("Vypršel časový limit. Vypočitali jste ",pocet_spravne," příkladů.")
        pred_vysledek = db.ziskej_data("SpeedyCalc")
        if  pred_vysledek == "Nan" or int(pred_vysledek) < pocet_spravne:
            print("Gratulujeme! Váš osobní rekord!")
            db.aktualizuj_data(pocet_spravne, "SpeedyCalc")            
        else:
            print("Váš osobní rekord je: "+str(pred_vysledek)+" pokusů.")
        db.zobraz_graf("SpeedyCalc", pocet_spravne)
        input("Stisknutím klávesy Enter se vrátíte do menu.")
        self.speedyCalc()
        
    def typeRace(self):
        self.loading("TypeRace")
        tprint("TypeRace")
        volani = menufun.zobraz_menu(["Hrát kompetitivní hru", "Ukončit hru"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            time.sleep(1)
            self.hlavni_menu()
        else:
            volani()
        texty = ["Posrat, nasrat, podesrat a nadsrat", "Kadění to je to pravý okay", "Turbosračka umí létat jako pes", "Kaděníčko smaženíčko ohřeje sluníčko", "Tulení kadění je ale libový", "Náš Matěj ten ho má ale dlouhatej"]
        pocet = 1
        start = time.time()
        while pocet < 4+1:
            rnd_text = random.choice(texty)
            while True:
                print(rnd_text)
                odpoved = input()
                if odpoved == rnd_text:
                    print("Správně %s/4"%pocet)
                    pocet+=1
                    break
                else:
                    pass
        end = time.time()
        vysledek = round(end - start, 2)
        print("Tvůj čas: ",vysledek,"s")
        pred_vysledek = db.ziskej_data("TypeRace")
        if  pred_vysledek == "Nan" or int(pred_vysledek) < vysledek:
            print("Gratulujeme! Váš osobní rekord!")
            db.aktualizuj_data(vysledek, "TypeRace")            
        else:
            print("Váš osobní rekord je: "+str(pred_vysledek)+" pokusů.")
        db.zobraz_graf("TypeRace", vysledek)
        input("Stisknutím klávesy Enter se vrátíte do menu.")
        self.typeRace()
    
    def nuficivsZombies(self):
        clearConsole()
        self.loading("Ňufící vs Zombies [¬º-°]¬")
        tprint("Nufici vs Zombies")
        print("Zachraňte co nejvíce ňufíků před spáry zombíků, než vyprší časový limit! Pro zastřelení zombíka odešlete jakýkoliv znak a pro záchranu ňufíka zmáčkněte pouze Enter.")
        print("Bodování:\n Záchrana ňufíka/zastřelení zombie = +1 bod\n Nezastřelení zombie/zastřelení ňufíka = -3 body\n")
        volani = menufun.zobraz_menu(["Hrát kompetitivní hru", "Ukončit hru"])
        if volani == False:
            print("Zadali jste hodnotu mino rozsah!")
            time.sleep(1)
            self.hlavni_menu()
        else:
            volani()
        seznam_obr = [zombie, zombie, zombie, zombie, kocka, doge, kralik]
        pocet_kol = 0
        skore = 0
        start = time.time()
        konec = 0
        while int(konec - start) < 15:
            rnd_obr = random.choice(seznam_obr)
            print(rnd_obr)
            odpoved = input()
            if len(odpoved) > 0:
                if rnd_obr == zombie:
                    print("Střelil jsi Zombie +1")
                    skore+=1
                else:
                    print("Střelil jsi Ňufíka -3")
                    skore-=3
            elif len(odpoved) == 0:
                if rnd_obr == zombie:
                    print("Nestřelil jsi Zombie -3")
                    skore-=3
                else:
                    print("Ňufík přežil +1")
                    skore+=1
            print("Skore: ", skore)
            pocet_kol+=1
            konec = time.time()
            
        print("Celkové skore: ",skore)
        vysledek = skore
        pred_vysledek = db.ziskej_data("NuficivsZombies")
        if  pred_vysledek == "Nan" or int(pred_vysledek) < vysledek:
            print("Gratulujeme! Váš osobní rekord!")
            db.aktualizuj_data(vysledek, "NuficivsZombies")            
        else:
            print("Váš osobní rekord je: "+str(pred_vysledek)+" pokusů.")
        db.zobraz_graf("NuficivsZombies", vysledek)
        input("Stisknutím klávesy Enter se vrátíte do menu.")
        self.nuficivsZombies()
    
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')         
menu = MenuSeznam()
db = Databaze()
hry = Hry()
menufun = MenuFunkce()

if __name__ == "__main__":
    menu.povoleni_vstup()

        
   