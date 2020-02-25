"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

# Sayı tutulup 3 hakta bulduran program
import random

tutulanSayi = random.randrange(1, 100)
print(tutulanSayi)

x = 0
tahmin = 0
hak = int(input("Hak sayısını giriniz: "))
puan = 100
hesapla = puan // hak

print(f"hak sayısı puanı: {puan}")

while x < hak and tutulanSayi != tahmin:
    
    x += 1
    tahmin = (int(input(f"{x}.Tahminizi girin: ")))
    
    if tutulanSayi == tahmin:
        print(f"{x}. Hakkınızda bildiniz ve {puan} puan kazandınız.")

    elif tutulanSayi < tahmin:
        puan = (puan - hesapla)
        print(f"Aşağı. -> {puan} puan kaldı.") 
        
    elif tutulanSayi > tahmin:
        puan = (puan - hesapla)
        print(f"Yukarı. -> {puan} puan kaldı.")
    
    elif x == hak:
        print(f"{hak} Hak sayınız bitti {puan} puanla kaybettiniz.")
else:
    print("Oyun bitti")