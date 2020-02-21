


# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise yada üniversite olmalıdır.
# name = input("İsim: ")
# years = int(input("Yaş: "))
# edu = input("Eğitim: ")

# if (years > 17) and (edu == "lise") or (edu == "üniversite"):
#     print(f"{name} {years} yaşında ve {edu} mezunu ehliyet alabilir")
# else:
#     print(f"{name} {years} ve {edu} mezunu ehliyet alamaz")
# yada #####################################################################
# if (yas>=18):
#     if (edu=="lise" or edu=="üniversite"):
#         print(f"{name} ehliyet alabilirsin.")
#     else:
#         print(f"{name} ehliyet alamazsın eğitim durumun yetersiz.")
# else:
#     print(f"{name} ehliyet alamazsın yaşın tutmuyor.")
#####################################################################################################################################
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığını karşılık gelen not bilgisini yazdırınız.
# 0 -24  => 0
# 25-44  => 1
# 45-54  => 2
# 55-69  => 3 
# 70-84  => 4
# 85-100 => 5

# yazili1 = float(input("1. Yazılı: "))
# yazili2 = float(input("2. Yazılı: "))
# sozlu = float(input("Sözlü: "))

# ortalama = (yazili1+yazili2+sozlu)/3
# print(ortalama)

# if (0 < ortalama < 24 ):
#     print(f"Öğrencinin 1. Yazılı sonucu: {yazili1} 2.Yazılı sonucu: {yazili2} sözlü sonucu: {sozlu} ortalaması: {ortalama} olduğu için geçme notu 0")
# elif (25 < ortalama < 44):
#     print(f"Öğrencinin 1. Yazılı sonucu: {yazili1} 2.Yazılı sonucu: {yazili2} sözlü sonucu: {sozlu} ortalaması: {ortalama} olduğu için geçme notu 1")
# elif (45 < ortalama < 54):
#     print(f"Öğrencinin 1. Yazılı sonucu: {yazili1} 2.Yazılı sonucu: {yazili2} sözlü sonucu: {sozlu} ortalaması: {ortalama} olduğu için geçme notu 2")
# elif (55 < ortalama < 69):
#     print(f"Öğrencinin 1. Yazılı sonucu: {yazili1} 2.Yazılı sonucu: {yazili2} sözlü sonucu: {sozlu} ortalaması: {ortalama} olduğu için geçme notu 3")
# elif (70 < ortalama < 84):
#     print(f"Öğrencinin 1. Yazılı sonucu: {yazili1} 2.Yazılı sonucu: {yazili2} sözlü sonucu: {sozlu} ortalaması: {ortalama} olduğu için geçme notu 4")
# elif (85 < ortalama < 100):
#     print(f"Öğrencinin 1. Yazılı sonucu: {yazili1} 2.Yazılı sonucu: {yazili2} sözlü sonucu: {sozlu} ortalaması: {ortalama} olduğu için geçme notu 5")

# yada##########################################################################################################################################################

# if (ortalama>=0) and (ortalama<25):
#     print(f"ortalamanız: {ortalama} notunuz: 0")
# elif (ortalama>=25) and (ortalama<45):
#     print(f"ortalamanız:{ortalama} notunuz: 1")
# elif (ortalama >= 45) and (ortalama < 55):
#     print(f"ortalamanız:{ortalama} notunuz: 2")
# elif (ortalama >= 55) and (ortalama < 70):
#     print(f"ortalamanız:{ortalama} notunuz: 3")
# elif (ortalama >= 70) and (ortalama < 85):
#     print(f"ortalamanız:{ortalama} notunuz: 4")
# elif (ortalama >= 85) and (ortalama < 100):
#     print(f"ortalamanız:{ortalama} notunuz: 5")
# else:
#     print("yanlış bilgi girdiniz.")
##########################################################################################################################################################
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1. Bakım => 1. yıl 365 güne kadar
# 2. Bakım => 2. yıl 365*2
# 3. Bakım => 3. yıl 365*2 and 365*3
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# *** datetime modülünü kullanmanız gerekiyor.

# days = int(input("aracınız kaç gündür trafikte: "))

# if days <= 365:
#     print("1.servis aralığı")
# elif days > 365 and days <= 365 * 2:
#     print("2.servis aralığı")
# elif days > 365 * 2 and days <= 365 * 3:
#     print("3.servis aralığı")
# else:
#     print("hatalı süre bilgisi.")

import datetime

tarih = input("aracınız hangi tarihte trafiğe çıktı (2019/8/9): ")

tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1.servis aralığı")
elif days > 365 and days <= 365 * 2:
    print("2.servis aralığı")
elif days > 365 * 2 and days <= 365 * 3:
    print("3.servis aralığı")
else:
    print("hatalı süre bilgisi.")










