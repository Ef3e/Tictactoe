import random
import os
sayilar = []
cizgiler = []
def ekle(dene = ""):
    if dene == "sil":
        cizgiler.clear()
        sayilar.clear()
    for u in range(1,10):
        sayilar.append(u)
        cizgiler.append("-")
def yazdir_cizgiler():
    ekle()
    return f"{cizgiler[0:3]}   {sayilar[0:3]}\n{cizgiler[3:6]}   {sayilar[3:6]}\n{cizgiler[6:9]}   {sayilar[6:9]}"
os.system("cls")
print(yazdir_cizgiler())
class tictactoe:
    def yatay_kontrol(arg):
        if (cizgiler[0] == arg and cizgiler[1] == arg and cizgiler[2] == arg) or (cizgiler[3] == arg and cizgiler[4] == arg and cizgiler[5] == arg) or (cizgiler[6] == arg and cizgiler[7] == arg and cizgiler[8] == arg) or(cizgiler[0] == arg and cizgiler[3] == arg and cizgiler[6] == arg) or(cizgiler[1] == arg and cizgiler[4] == arg and cizgiler[7] == arg) or(cizgiler[2] == arg and cizgiler[5] == arg and cizgiler[8] == arg) or(cizgiler[0] == arg and cizgiler[4] == arg and cizgiler[8] == arg) or(cizgiler[2] == arg and cizgiler[4] == arg and cizgiler[6] == arg):
            return True
    def __init__(self):
        self.ilk_oyuncu = input("ilk oyuncunun isimi = ") #oyuncularin isimini aldik
        self.ikinci_oyuncu = input("ikinci oyuncunun isimi = ")  
        self.oyuncular = [self.ikinci_oyuncu,self.ilk_oyuncu]    
        self.x_oyuncu = random.choice(self.oyuncular)
        self.oyuncular.remove(self.x_oyuncu)
        self.o_oyuncu = self.oyuncular[0] 
        self.dogru = True
    def oyun(self):
        while self.dogru:
            dogru = True
            while dogru:
                try:
                    self.x_oyuncu_hamle = int(input(f"{self.x_oyuncu}(x) yer sec = "))
                    dogru = False
                except:
                    dogru = True
            while cizgiler[self.x_oyuncu_hamle-1] != "-":
                self.x_oyuncu_hamle = int(input(f"{self.x_oyuncu} bos bir yer sec = "))
            cizgiler[self.x_oyuncu_hamle-1] = "X"
            sayilar[self.x_oyuncu_hamle-1] = 0
            os.system("cls")
            print(yazdir_cizgiler())
            kontrol = tictactoe.yatay_kontrol("X")
            if kontrol == True:
                print(f"{self.x_oyuncu} oyunu kazandı")
                evet = input("bir daha oynamak istermisiniz = ").lower()
                if evet[0] == "e":
                    ekle("sil")
                    os.system("cls")
                    print(yazdir_cizgiler())
                    tictactoe().oyun()
                else:
                    exit()
            dogru = True
            while dogru:
                try:
                    self.o_oyuncu_hamle = int(input(f"{self.o_oyuncu}(O) yer secsin = "))
                    dogru = False
                except:
                    dogru = True
            while cizgiler[self.o_oyuncu_hamle-1] != "-":
                self.o_oyuncu_hamle = int(input(f"{self.o_oyuncu} bos bir yer sec = "))
            cizgiler[self.o_oyuncu_hamle-1] = "O"
            sayilar[self.o_oyuncu_hamle-1] = 0
            os.system("cls")
            print(yazdir_cizgiler())
            kontrol = tictactoe.yatay_kontrol("O")
            if kontrol == True:
                print(f"{self.o_oyuncu} oyunu kazandı")
                evet = input("bir daha oynamak istermisiniz = ").lower()
                if evet[0] == "e":
                    ekle("sil")
                    os.system("cls")
                    print(yazdir_cizgiler())
                    tictactoe().oyun()
                else:
                    exit()
tictactoe().oyun()
