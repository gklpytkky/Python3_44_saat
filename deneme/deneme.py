# import random

# def rastgeleSayi(sayi):
#     print(sayi)    
#     return

# sayi = random.randint(1, 10)

# rastgeleSayi(sayi)
##############################################
# def isimGir(isim,soyisim):
#     print(isim,soyisim)
#     return

# isim = input("İsminizi giriniz: ")
# soyisim = input("Soyisminizi giriniz: ")

# isimGir(isim,soyisim)
##############################################


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result


print("\n\nRecursion Example Results")
tri_recursion(6)
