"""
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi = float(input("sayı: "))
result = (sayi > 0) and (sayi <= 100)
print(f"sayı 0 100 arasında mı: {result}")
"""
# 1. cevap

# sayi = int(input("Bir sayı giriniz: "))
# if 0<sayi<100:
#     print(f"Girilen {sayi} sayısı 0-100 arasındadır")
# else:
#     print(f"Girilen {sayi} sayısı 0-100 arasında değildir.")

#######################################################################
"""
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input("sayı: "))
result = (sayi > 0) and (sayi % 2 == 0)
print(f"girilen sayı pozitif çift sayı mı: {result})

"""
# # 2. cevap
# sayi = int(input("Bir sayı giriniz: "))

# if (0 < sayi):
#     cift = (sayi %2 == 0)
#     if cift == True:
#         print(f"girilen {sayi} sayısı pozifit bir çift sayıdır")
#     else:
#         print(f"girilen {sayi} sayısı pozitif ama çift bir sayı değildir")
# else:
#     print(f"girilen {sayi} sayısı pozitif değildir ama bir çift sayıdır.")

#######################################################################
"""
3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = "email@sadikturan.com"
password = "abc123"

result = (girilenEmail == email) and (girilenPassword == password)
print(f"uygulamaya giriş başarılı mı: {result}")

"""
# 3. cevap
email = "email@sadikturan.com"
password = "abc123"

mailGiris = input("Email adresinizi girin: ")
passGiris = input("Parolanızı giriniz: ")



if email == mailGiris:
    if password == passGiris:
        print("Giriş yapıldı")
    else:
        print("Girilen parola bilgisi hatalıdır")
else:
    print("Girilen email ve parola bilgileri hatalıdır.")




#######################################################################
"""
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

result = (a > b) and (a > c)
print(f"a en büyük sayıdır : {result}")

result = (b > a) and (b > c)
print(f"b en büyük sayıdır : {result}")

result = (c > a) and (c > b)
print(f"c en büyük sayıdır : {result}")

"""

"""
5- Kullanıcıdan 2 vşze (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değişse kaldı yazdırın.
   a-) Ortalama 50 olsa bile filan notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input("vize 1: "))
vize2 = float(input("vize 2: "))
vize3 = float(input("vize 3: "))

ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
result = (ortalama >= 50) and (final >= 50)
result = (ortalama >= 50) or (final >= 70)

print(f"öğrencinin ortalaması : {ortalama} ve geçme durumu : {result}")

"""

"""
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   Formül : (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   0-18.4     => Zayıf
   18.5-24.9  => Normal
   25.0-29.9  => Fazla Kilolu
   30.0-34.9  => Şişman (Obez)

name = input("adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.4) and (index <= 24.9)
kilolu = (index >= 24.9) and (index <= 29.9)
obez = (index >= 29.9) and (index <= 34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {obez}")

"""
