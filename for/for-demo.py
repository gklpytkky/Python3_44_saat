# sayilar = [1,3,5,7,9,12,19,21]

# # 1- Sayılar listesindeki hangi sayılar 3'ün katıdır ?
# # 2- Sayilar listesinde sayıların toplamı kaçtır ?
# # 3- Sayılar listesindeki tek sayıların karesini alınız.
# ############################################################
# 1. cevap
# for i in sayilar:
#     if (i % 3 == 0):
#         print(i)

# print(50*"*")
# 2. cevap
# toplam = 0
# for t in sayilar:
#     toplam += t
# print(toplam)

# print(50*"*")
# 3. cevap
# for k in sayilar:
#     if (k % 2 == 1):
#         print(k**2)
#############################################################
# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
# # 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

# for i in sehirler:
#     if len(i) <= 5:
#         print(i)
#############################################################
# urunler = [
#     {"name" : "samsung S6", "price": "3000"},
#     {"name": "samsung S7", "price": "4000"},
#     {"name": "samsung S8", "price": "5000"},
#     {"name": "samsung S9", "price": "6000"},
#     {"name": "samsung S10", "price": "7000"}
# ]

# # 5- Ürünlerin fiyatları toplamı nedir ?
# # 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ? 

# toplam = 0
# for t in urunler:
#     toplam += int(t["price"])
# print(toplam)

# for a in urunler:
#     if (int(a["price"]) <= 5000):
#         print(a)
