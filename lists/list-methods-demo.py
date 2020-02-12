names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
result = names.append("Cenk")
print(names)

# 2-  "Sena" degerini listenin başına ekleyini.
result = names.insert(0, "Sena")
print(names)
##############################################
names.insert(len(names),"Mehmet")
print(names)

# 3-  "Deniz" ismini listeden siliniz.
result = names.remove("Deniz")
result = names.pop(3)
print(names)

# 4-  "Deniz" isminin indeksi nedir.
index = names.index("Deniz")
print(index)

# 5-  "Ali" listenin bir elemanı mıdır?
result = "Ali" in names
print(result)
#########################################
result = names.index("Ali")
print(result)

# 6-  Liste elemanlarını ters çeviriniz.
names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = ["Chevrolet"] , ["Dacia"]
print(str)
#####################################
str = "Chevrolet,Dacia"
result = str.split(",")
print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ? 
years.sort()
print(years)
result = years[0],years[3]
print(result)
#################################################
min = min(years)
max = max(years)
print(min,max)

# 11- years dizisinde kaç tane 1998 değeri vardır ?
result = years.index(1998)
print(result)
#########################################
result = years.count(1998)
print(result)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- kullanıcıdan alacağınız 4 tane marka bilgisini bir listede saklayınız. 
marka1 = input("1.Marka giriniz: ")
marka2 = input("2.Marka giriniz: ")
marka3 = input("3.Marka giriniz: ")
marka4 = input("4.Marka giriniz: ")
markalar = [marka1 , marka2 , marka3 , marka4]
print(type(markalar))
print(markalar)
#####################################
markalar = []

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

print(markalar)