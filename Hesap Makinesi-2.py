import os
import sys
import io

from math import *
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def karealma():
    karesialinan = float(input("Karesi alınacak sayı: "))
    karesi = karesialinan ** 2
    print(karesi)
def hipotenüs():
    kenar1 = float(input("1.Kenar: "))
    kenar2 = float(input("2.Kenar: "))
    hipo = (kenar1**2+kenar2**2)**0.5
    print("Hipotenüs: ",hipo)
def kupcevre():
    karekenar = float(input("Küpün 1 kenarını girin: "))
    karekenarcevre = 6* (karekenar ** 2)
    print("Çevre: ",karekenarcevre)
def kupalan():
    karekenara = float(input("Küpün 1 kenarını girin: "))
    karekenaralan = karekenara ** 3
    print("Küp: ",karekenaralan)
def dairecevre():
    pi = float(input("Varsayılan Pi: "))
    dairer = float(input("Yarı çap: "))
    dairecevresonuc = 2 * pi * dairer
    print(dairecevresonuc)
def dairealan():
    pi = float(input("Varsayılan Pi: "))
    dairer = float(input("Yarı çap: "))
    dairealansonuc = pi * (dairer ** 2)
    print(dairealansonuc)
def faktoriyel():
    sayi = int(input("Sayı: "))
    fakt = 1
    for i in range(2,sayi+1):
        fakt *= i
    print(fakt)

print("""****************************************

Hesap Makinesi

[1] Toplama

[2] Çıkarma

[3] Çarpma

[4] Bölme

[5] Kare Alma

[6] Hipotenüs

[7] Küp Çevre Hesaplama

[8] Küp Alan Hesaplama

[9] Daire Çevre Hesaplama

[10] Daire Alan Hesaplama

[11] Faktöriyel

[12] Papağan

[q] Çıkış

****************************************
""")
    
while True:

    islem = input("İşlem Seçiniz: ")

    if (islem == "q"):
        print("Çıkış Yaptınız.")
        break
    
    elif (islem == "1"):
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print(toplama(a,b))
    
    elif (islem == "2"):
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print(cikarma(a,b))

    elif (islem == "3"):
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print(carpma(a,b))

    elif (islem == "4"):
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print(bolme(a,b))

    elif (islem == "5"):
        karealma()
    
    elif (islem == "6"):
        hipotenüs()
    
    elif (islem == "7"):
        kupcevre()

    elif (islem == "8"):
        kupalan()

    elif (islem == "9"):
        dairecevre()
    
    elif (islem == "10"):
        dairealan()
    
    elif (islem == "11"):
        faktoriyel()

    elif (islem == "12"):
        os.system("curl parrot.live")