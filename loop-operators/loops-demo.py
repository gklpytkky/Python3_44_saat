"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

import random

tutulanSayi = random.randrange(1, 100)
print(tutulanSayi)

tahmin = int(input("Tahmininizi Girin: "))
x = 0
while x < 100:
    x += 1
    if tutulanSayi == tahmin:
    print("Sayıyı buldunuz")
        

    


