# 1- Girilen 2 sayıdan hangisi büyüktür ?
# sayi1 = int(input("sayı gir: "))
# sayi2 = int(input("sayı gir: "))
# result = (sayi1 > sayi2)
# print(f"{sayi1} değeri {sayi2} değerinden büyükmüdür : {result}")

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
# #    Eger ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# vize1 = float(input("1.vize notu girin: "))
# vize2 = float(input("2.vize notu girin: "))
# final = float(input("final notu girin: "))
# a = ((int(vize1) + int(vize2))/2 * 0.6) 
# print("vize notu %60:",a)
# b = (final * 0.4)
# print("final notu %40: ",b)
# son = ((a+b)/2)
# print(son)
# print(son >= 50)
################################################################
# vize1 = float(input("1.vize:"))
# vize2 = float(input("2.vize:"))
# final = float(input("final:"))
# ortalama = (((vize1 + vize2) * 0.6)/2) + (final * 0.4)
# print(f"not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama >=50}")

# 3- Girilen bir sayının tek mi çift mi olduğnu yazdırınız.
# a = int(input("Bir sayı giriniz: "))
# print(a % 2 == 0)
# ############################################
# sayi = int(input("sayı: "))
# tekcift = (sayi % 2 == 0)
# print(f"girilen sayı çift olma durumu: {tekcift}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# a = int(input("Bir sayı giriniz : "))
# print(a >= 0)
############################################
# sayi = int(input("sayı: "))
# pozitifmi = (sayi > 0)
# print(f"girilen sayının pozitif olma durumu: {pozitifmi}")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email : email@sadikturan.com parola:abc123)

# email = input("Email yazınız: ")
# parola = input("Parola giriniz: ")

# a = (email == "email@sadikturan.com")
# b = (parola == "abc123")

# print(a,b)
#################################################
# email = "email@sadikturan.com"
# password = "abc123"

# girilenEmail = input("email: ")
# girilenPassword = input("parola: ")
# isEmail = (email == girilenEmail.lower().strip())
# isPassword = (password == girilenPassword.lower())
# print(f"email bilgisi doğrumu: {isEmail} ve parola doğru mu : {isPassword}")

