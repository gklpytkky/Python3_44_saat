"""
    1- Bir müşretinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşreti adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""

musteriAdi = "Gokalp"
musteriSoyadi = "Yatıkkaya"
musteriAdSoyad = "Gokalp" + " " + "Yatıkkaya"
print(musteriAdSoyad)
musteriCinsiyet = "Erkek"
MusteriTc = "321321321"
musteriDogum = 1984
musteriAdres = "İzmir Balçova"
musteriYas = 2019 - musteriDogum

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""
order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3
print("total: " , total)