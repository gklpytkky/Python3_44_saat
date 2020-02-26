"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

"""
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
        break
    elif tutulanSayi < tahmin:
        puan = (puan - hesapla)
        print(f"Aşağı. -> {puan} puan kaldı.")

    elif tutulanSayi > tahmin:
        puan = (puan - hesapla)
        print(f"Yukarı. -> {puan} puan kaldı.")

    if x == hak:
        print(f"{hak} Hak sayınız bitti {puan} puanla kaybettiniz. Tutulan sayı: {tutulanSayi}")


"""

# import random

# sayi = random.randint(1, 10)
# can = int(input('kaç hak kullanmak istersiniz: '))
# hak = can
# sayac = 0

# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('tahmin: '))

#     if sayi == tahmin:
#         print(
#             f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1) }')
#         break
#     elif sayi > tahmin:
#         print('yukarı')
#     else:
#         print('aşağı')
#     if hak == 0:
#         print(f'hakkınız bitti. Tutulan sayı : {sayi}')


"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

import random

tutulanSayi = random.randint(1, 10)
x = 0
hak = int(input("Kaç tahmin hakkı istersiniz: "))
sayac = 0
puan = 100

while x < hak:
    x += 1
    sayac += 1
    tahmin = int(input("Tahminizi giriniz: "))
    if tahmin == tutulanSayi:
        print(f"Sayıyı {sayac}. hakkınızda buldunuz. {puan-(puan/hak) * (sayac-1)}")
        break
    elif tahmin < tutulanSayi:
        print("Yukarı")
    elif tahmin > tutulanSayi:
        print("Aşağı")
    if x == hak:
        print(f"Tahmin hakkınız bitti. Tutulan sayı {tutulanSayi}")
