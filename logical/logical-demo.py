# 1- Girilen bir sayının  0-100 arasında olup olmadığnı kontrol ediniz.
# sayi = int(input("Sayi: "))
# result = (0 < sayi) and (sayi <= 100)
# print(f"Girilen {sayi} sayısı 0 ile 100 arasında mıdır? {result}")
######################################################################
# 2- Girilen bir sayının pozitif çift sayı olup olmadığnı kontrol ediniz.
# sayi = int(input("Sayi: "))
# result = (sayi > 0) and (sayi %2 == 0)
# print(f"Girilen sayi {sayi} pozitif bir çift sayı mı: {result}")
######################################################################
# 3- Email ve parola bilgileri ile giriş kontrolü yapını.
# email = "asdasd@asd.com"
# password = "asd123"
# emailGiris = input("Email girinis: ")
# passwordGiris = input("Parola girini: ")
# result = (emailGiris == email) and (passwordGiris == passwordGiris)
# print(f"Email bilgisi {emailGiris} ve password bilgisi {passwordGiris} doğru mu :{result}")
######################################################################
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# sayi1 = int(input("Bir sayı giriniz: "))
# sayi2 = int(input("Bir sayı giriniz: "))
# sayi3 = int(input("Bir sayı giriniz: "))
# result = (sayi1<sayi2<sayi3) or (sayi1>sayi2>sayi3)
# print(result)
######################################################################
# a =int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# result = (a > b) and  (a > c)
# print(f"a en büyük sayıdır:{result}")

# result = (b > a) and (b > c)
# print(f"b en büyük sayıdır:{result}")

# result = (c > a) and (c > b)
# print(f"c en büyük sayıdır:{result}")
######################################################################
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# vize1 = float(input("1.vize notu: "))
# vize2 = float(input("2.vize notu: "))
# final = float(input("final notu: "))
# ortalama = ((vize1 + vize2)/2) * 0.6 + (final * 0.4)
# print(ortalama)
# a = (ortalama >= 50) and (final >= 50) or (final == 70) 
# print(a)
######################################################################
# vize1 = float(input("1.vize notu: "))
# vize2 = float(input("2.vize notu: "))
# final = float(input("final notu: "))

# ortalama = ((vize1 + vize2)/2) * 0.6 + (final * 0.4)
# result = (ortalama >= 50) and (final >= 50)
# result = (ortalama >=50) or (final >= 70)

# print(f"Öğrencinin ortalaması: {ortalama} ve gçme durumu: {result")
######################################################################
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formul : (Kilo / boy uzunluğunun karesi)
#    Aşağıda ki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4   => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman(obez)
# ad = input("Adınızı Giriniz: ")
# kilo = float(input("Kilonuzu Giriniz: "))
# boy = int(input("Boyunuzu Giriniz: "))
# formul = (kilo) / (boy ** 2) 
# print(formul)
# print(0 <= formul <= 18.4, "Zayıf") or (18.5 <= formul <= 24.9, "Normal") or (25.0 <= formul <= 24.9, "Fazla Kilolu") or (30.0 <= formul <= 34.9, "Fazla Kilolu")
######################################################################
name = input("Adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
fazla_kilolu = (index >= 25.0) and (index <= 29.9)
sisman_obez = (index >= 30.0) and (index <= 34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {fazla_kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {sisman_obez}")
