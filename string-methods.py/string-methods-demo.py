website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


"""
# 1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlini silin.

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.

# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın.

# 4- "website" içinde kaç tane a karakteri vardır? (count("a"))

# 5- "website" www" ile başlayıp com ile bitiyor mu?

# 6- "website" içinde ".com" ifadesi var mı?

# 7- "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

# 8- "Content" ifadesini satırda 50 karakter içine yerleştirip sağ ve soruna * ekleyiniz.

# 9- "course" karakter dizisindeki tüm boşluk karakterlini "-" ile değiştirin.

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.

# 11- "course" karakter dizisini boşluk karkterlinden ayırın.
"""

# 1.cevap
s = " Hello World ".replace(" ","")
print(s)
####################################
result = " Hello World ".strip()
result = " Hello World ".lstrip()
result = " Hello World ".rstrip()
####################################
result = website.lstrip("/:pth")
print(result)

# 2.cevap
s = "www.sadikturan.com".replace("www.","").replace(".com","")
print(s)
####################################
result = "www.sadikturan.com".strip("w.moc")
print(result)

# 3.cevap
result = course.lower()
result = course.upper()
result = course.title()
print(result)

# 4.cevap
a = website.count("a")
b = website.count("www")
c = website.count("www",0,10)
print(a,b,c)

# 5.cevap
a = website.startswith("www")
b = website.endswith("com")
print(a,b)

# 6.cevap
result = website.index(".com")
print(result)
####################################
a = website.find(".com")
b = website.find(".com",0,10)
b = course.find("Python")
c = course.rfind("Python")
d = website.index("com")
print(a,b,c,d)

# 7.cevap
a = course.isdigit()
b = course.isalpha()
print(a,b)

# 8.cevap
a = "Contents".center(50,"*")
b = "Contents".ljust(50,"*")
c = "Contents".rjust(50,"*")
print(a,b,c)

# 9.cevap
a = course.replace(" ","-")
b = course.replace(" ","-",5)
print(a,b)

# 10.cevap
s ="Hello World".replace("World","There")
print(s)

# 11.cevap
a = course.split(" ")
# result = result[2]
a = a[5]
print(a)





