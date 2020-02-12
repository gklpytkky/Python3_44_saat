website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
"""
# 1- "course" karakter dizisinde kaç karakter bulunmaktadır.?

# 2- "website" içinde www karakterlerini alın.

# 3- "website" içinde com karakterlerini alın.

# 4- "course" içinde ilk 15 ve son 15 karakterlerini alın.

# 5- "course" ifadesindeki karakterleri tersten yazdırın.

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."

# 7- "Hello world" ifadesindeki w hargini "W" ile değiştirin.

# 8-"abc" ifadesini yan yana 3 defa yazdırın. 
"""

# 1 soru
print("Course karakter dizinde",len(course),"karakter bulunmaktadır.")
# result = len(course)
# print(result)

# 2 soru
print(website[7:10])

# 3 soru
print(website[22:25])
# length = len(website)
# result = website[length-3:length]
# print(result)


# 4 soru
print(course[:15])
print(course[-15:])

# 5 soru
print("course"[::-1])

# 6 soru
name = "Bora"
surname = "Yılmaz"
age = "32"
job = "mühendis"

print(f"Benim adım {name} {surname} Yaşım {age} ve mesleğim {job}")
# result = "Benim adım "+ name+" " + surname + ",Yaşım "+ age +" ve mesleğim " +job
# print(result)
# result = "Benim adım {} {},Yaşım {} ve mesleğim {}.".format(name,surname,age,job)
# print(result)
# result = f"Benim adım {name} {surname},Yaşım {age} ve mesleğim {job}."
# print(result)

# 7 soru
string = "Hello world"
print(len(string))
print(string.title())
# s = "Hello world"
# s = s[0:6] + "W"+ s[-4:]
# print(s)

# 8 soru 
print("abc "*3)
# result = "abc "*3
# print(result)