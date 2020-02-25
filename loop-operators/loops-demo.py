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

while x < 5 and tutulanSayi != tahmin:
    x += 1
    tahmin = (int(input(f"{x}.Tahminizi girin: ")))
    if tutulanSayi == tahmin:
        print("Bildiniz.")
    elif tutulanSayi < tahmin:
        print("Aşağı")
    elif tutulanSayi > tahmin:
        print("Yukarı")
    if x == 5:
        print("hakkınız bitti")



    
    


