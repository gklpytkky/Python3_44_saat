sayilar = [1,3,5,7,9,12,19,21]

# 1: Sayılar listesini while ile ekrana yazdırın.
# x = 0
# while x < 1:
#     print(sayilar)
#     x += 1
# ##################################################
# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

# basla = int(input("başlangıç değeri: "))
# bitis = int(input("bitiş değeri: "))

# while basla < bitis:
#     basla += 1
#     if basla % 2 == 1:
#         print(basla)
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

# sayi = 100

# while sayi > 0:
#     sayi -= 1
#     print(sayi)

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# numbers = []
# i = 0
# while i < 5:
#     sayi = int(input(f'{i}.sayıyı girin: '))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı(name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

# urunler = []

# adet = int(input('kaç ürün eklemek istiyorsunuz: '))

# i = 0

# while(i < adet):
#     name = input('ürün ismi: ')
#     price = input('ürün fiyatı: ')
#     urunler.append({
#         'name': name,
#         'price': price
#     })
#     i += 1

# for urun in urunler:
#     print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')
