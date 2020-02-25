
# Sayı tutulup 3 hakta bulduran program
# import random

# tutulanSayi = random.randrange(1, 100)
# print(tutulanSayi)

# x = 1

# while x < 4:
#     tahmin = (int(input(f"{x}. Tahmininizi girin: ")))
#     x += 1
#     if tutulanSayi == tahmin:
#         print("Sayıyı buldunuz.:D..")
#     elif x == 4:
#         print("Hakkınız bitti.!!.")
"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""
# v2.0

import random

tutulanSayi = random.randrange(1, 100)
print(tutulanSayi)

x = 0

while x < 5:
    tahmin = (int(input(f"Tahmininizi girin: ")))
    x += 1
    if x == 5:
       print("Hakkınız bitti..")
    elif tutulanSayi < tahmin:
        print("Aşağı")
    elif tutulanSayi > tahmin:
        print("Yukarı")
    elif tutulanSayi == tahmin:
        print(f"Tebrikler tutulan {tutulanSayi} sayıyısını buldunuz..:D...")
    


