x, y, z, = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x.y.z toplamının farkı nedir
# sayi1 = input("Bir sayı giriniz: ")
# sayi2 = input("Bir sayı giriniz: ")

# carpim = int(sayi1) * int(sayi2)
# print("iki sayının çarpımı:",carpim)

# toplam = x + y + z
# print("x,y,z sayıları toplamı :", toplam)

# fark = carpim - toplam
# print("uzun fark:" ,fark)
# ##########################################
# fark_yeni = (int(sayi1) * int(sayi2)) - (x+y+z)
# print("kısa fark: " ,fark_yeni)
# ##########################################
# a = int(input("1.sayı: "))
# b = int(input("2.sayı: "))
# result = (a * b)-(x+y+z)
# print(result)

# 2- y'nin x'e kalansız bölümünü hesaplayınız.
bolum = y // x
print("*"*50)
print(f"{y} değerinin {x} değerine kalansız bölümü: ",bolum)

# 3- (x,y,z) toplamının mod 3' ü nedir ?
topla = x + y +z
print("*"*50)
print("x,y,z toplam:" ,topla)
mod = topla%3
print(f"{x}, {y}, {z} değerleri toplamının 3. modu: ", mod)
#########################################
mod = (x + y + z) % 3
print(f"{x}, {y}, {z} değerleri toplamının 3. modu: ",mod)

# 4- y'nin x. kuvvetini hesaplayınız.
kuvvet = y**x
print("*"*50)
print(f"{y} değerinin {x}. kuvveti :",kuvvet)

# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır.
x, *y, z = numbers
kup = z**3
print("*"*50)
print("z değeri küpü:",kup)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır
x, *y, z = numbers
print("*"*50)
print("y değeri içerği:",y[:3])
toplamaY = y[0] + y[1] + y[2]
print("y değerinin toplamı:" ,toplamaY)
