# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
liste = ["Bmw","Mercedes","Opel","Mazda"]
print(liste)
############################################
arabalar = ["Bmw","Mercedes","Opel","Mazda"]

# 2-  Liste kaç elemanlıdır ?
print(len(liste))
############################################
result = (len(arabalar))

# 3-  Listenin ilk ve son elemanı nedir ?
print(liste[0])
print(liste[-1])
############################################
result = arabalar[0]
result = arabalar[3]
result = arabalar[-1]

# 4-  Mazda değerini Toyota ile değiştirin.
liste.remove("Mazda")
liste.insert(3,"Toyota")
print(liste)
############################################
arabalar[-1] = "Toyota"
result = arabalar

# 5-  Mercedes listenin bir elemanı mıdır ?
a = liste.index("Mercedes")
print(a)
##############################################
result = "Mercedes" in arabalar

# 6-  Listenin -2 indeksinde ki değer nedir ?
print(liste[-2])
#############################################
result = arabalar[-2]

# 7-  Listenin ilk 3 elemanını alın.
print(liste[:3])
#############################################
result = arabalar[:3]
result = arabalar[0:3]

# 8-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" degerlerini ekleyin.
print(liste)
liste.remove("Toyota")
liste.insert(2,"Toyota")
liste.remove("Opel")
liste.insert(3,"Renault")
print(liste)
##################################################
arabalar[-2:] = ["Toyota","Renault"]
result = arabalar

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
print(liste)
liste.append("Audi")
liste.append("Nissan")
print(liste)
###################################################
result = arabalar + ["Audi","Nissan"]

# 10- Listenin son elemanını silin.
print(liste)
liste.remove("Nissan")
print(liste)
#####################################################
del arabalar[-1]
result = arabalar

# 11- Liste elemanlarını tersten yazdırınız.
liste.reverse()
print(liste)
#####################################################
result = arabalar[::-1]

# 12- Aşağıda ki verileri bir liste içinde saklayınız.

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90)
        
studentA = ["Yiğit", "Bilgi", 2010 , [70,60,70]]
studentB = ["Sena", "Turan", 1999 , [80,80,70]]
studentC = ["Ahmet", "Turan", 1998 , [80,70,70]]


# 13- Liste elemanlarını ekrana yazdırınız.
result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yasinda ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3 }"
#######################################################



######################################################
print(result)