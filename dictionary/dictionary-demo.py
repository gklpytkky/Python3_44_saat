"""
    ogrenciler =
     {
        
        "120": 
        {
            "ad" : "Ali",
            "soyad":"Yılmaz",
            "telefon":"532 000 00 01"
        },
        
        "125": 
        {
            "ad":"Can",
            "soyad":"Korkmaz",
            "telefon":"532 000 00 02"
        },
       
        "128":
        {
            "ad":"Volkan",
            "soyad":"Yükselen",
            "telefon":"532 000 00 03"
        },
   
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz.

"""
# 1- cevap:

ogrenciler = {}

numara = input("Öğrenci no : ")
isim = input("Öğrenci Adı : ")
soyad = input("Öğrenci Soyadı : ")
telefon = input("Öğrenci Telefonu : ")

# ogrenciler[numara] = {
#     "ad" : isim,
#     "soyad" : soyad,
#     "telefon" : telefon
# }
ogrenciler.update({
    numara: {
        "ad" : isim,
        "soyad" : soyad,
        "telefon" : telefon
    }
})

numara = input("Öğrenci no : ")
isim = input("Öğrenci Adı : ")
soyad = input("Öğrenci Soyadı : ")
telefon = input("Öğrenci Telefonu : ")

ogrenciler.update({
    numara: {
        "ad": isim,
        "soyad": soyad,
        "telefon": telefon
    }
})

numara = input("Öğrenci no : ")
isim = input("Öğrenci Adı : ")
soyad = input("Öğrenci Soyadı : ")
telefon = input("Öğrenci Telefonu : ")

ogrenciler.update({
    numara: {
        "ad": isim,
        "soyad": soyad,
        "telefon": telefon
    }
})

print("*"*50)

# 2- cevap:

ogrNo = input("öğrenci no:")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefon ise {ogrenci['telefon']}")
