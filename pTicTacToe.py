import random
import os 
class oyuncular():
    def __init__(self,oyuncu1 = "",oyuncu2 = ""):
        self.bir = oyuncu1
        self.iki = oyuncu2   
    def random_oyuncu(self):
        self.liste = [
            self.bir,
            self.iki
        ]
        return self.liste
def yaz(arg):
    sayilar = []
    for u in range(1,10):
        sayilar.append(u)
    os.system("cls")
    print(f"{arg[0:3]}    {sayilar[0:3]}\n{arg[3:6]}    {sayilar[3:6]}\n{arg[6:9]}    {sayilar[6:9]}")
class Tic_tac_toe():
    def __init__(self):
        os.system("cls")
        self.cizgilerr = Tic_tac_toe.cizgiler()
        self.oyuncular = Tic_tac_toe.random_oyuncu_sec()
        self.x_oyuncusu = self.oyuncular[0]
        self.y_oyuncusu = self.oyuncular[1]
        self.cizgilere_yerles()
    def cizgiler():
        cizgilerlist = []
        for u in range(9):
            cizgilerlist.append("-")
        return cizgilerlist
    def random_oyuncu_sec():
        birinci_oyuncu_isim = input("Oyuncu isimi:")
        ikinci_oyuncu_isim = input("ikinci oyuncu isimi:")
        oyuncular_liste = oyuncular(birinci_oyuncu_isim,ikinci_oyuncu_isim).random_oyuncu()
        oyunculari = []
        for u in range(len(oyuncular_liste)):
            a = random.choice(oyuncular_liste)
            oyunculari.append(a)
            oyuncular_liste.remove(a)
        return oyunculari
    def cizgilere_yerles(self):
        yaz(self.cizgilerr)
        self.deneg = True
        while self.deneg:
            self.x_yer = int(input(f"(x) {self.x_oyuncusu} lutfen yerinizi seciniz:"))
            while self.cizgilerr[self.x_yer-1] != "-":
                self.x_yer = int(input(f"(x) {self.x_oyuncusu} lutfen yerinizi seciniz:"))
            else:
                self.cizgilerr[self.x_yer-1] = "X"
            yaz(self.cizgilerr)
            self.kontrol("X")
            self.y_yer = int(input(f"(O) {self.y_oyuncusu} lutfen yerinizi seciniz:"))
            while self.cizgilerr[self.y_yer-1] != "-":
                self.y_yer = int(input(f"(O) {self.y_oyuncusu} lutfen yerinizi seciniz:"))
            else:
                self.cizgilerr[self.y_yer-1] = "O"
            self.kontrol("O")
            yaz(self.cizgilerr)
    def kontrol(self,arg):
        if self.cizgilerr.count("-") < 1:
            print("Berabere kalindi")
            self.sor()
        if (self.cizgilerr[0] == arg and self.cizgilerr[1] == arg and self.cizgilerr[2] == arg) or (self.cizgilerr[3] == arg and self.cizgilerr[4] == arg and self.cizgilerr[5] == arg) or (self.cizgilerr[6] == arg and self.cizgilerr[7] == arg and self.cizgilerr[8] == arg) or(self.cizgilerr[0] == arg and self.cizgilerr[3] == arg and self.cizgilerr[6] == arg) or(self.cizgilerr[1] == arg and self.cizgilerr[4] == arg and self.cizgilerr[7] == arg) or(self.cizgilerr[2] == arg and self.cizgilerr[5] == arg and self.cizgilerr[8] == arg) or(self.cizgilerr[0] == arg and self.cizgilerr[4] == arg and self.cizgilerr[8] == arg) or(self.cizgilerr[2] == arg and self.cizgilerr[4] == arg and self.cizgilerr[6] == arg):
            if arg == "O":
                kazanan = self.y_oyuncusu
            else:
                kazanan = self.x_oyuncusu
            print(f"({arg}) {kazanan} oyuncusu kazandi")
            self.sor()
    def sor(self):
        evet = input("Bir daha oynamak istermisiniz E/H:")
        if evet[0].lower() == "e":
            Tic_tac_toe()
        else:
            exit()
Tic_tac_toe()
