# print
print("Tugba")
print("Tugba", "ornek", "T", "B", "M", sep='.')

# değişkenler ve type()
a = "ali"
b = 5
print(type(a))
print(type(b))

# string tanımlama örnekleri
"string tanımlama"
"""
çoklu
yorum satırı
"""

# veri tipleri
a = 5
print(type(a))      # int
b = "Tugba"         # str
c = 3.5             # float
d = 'k'             # karakter

# veri yapıları: list / tuple / dict / set
liste1 = [1, 3, 3, 5, 4, 5, 4, "ali", "canan"]
print(liste1[0])
print(len(liste1))

liste2 = [1, 3, 3, 5, 4, 5, 4]
liste2.sort()
print(liste2)
liste2[0] = 100000          # list mutable
print(liste2[0])
print(liste2)
liste2.pop()
liste2.append(25)
liste2.insert(7, "25")
print(liste2)
print(liste2[7])

demet = ("ali", "ayşe")
print(demet)
print(len(demet))
print(demet[0])
print(demet.count("ali"))
print(demet.index("ali"))

# basit fonksiyon örnekleri
x = "Tugba"
print(type(x))
print(x.capitalize())

def topla_iki(deger, deger2):
    print("{}, {} degerlerini alır".format(deger, deger2))

def topla_parametre(p):
    print("alınan deger:", p)

topla_parametre(5)
topla_iki(3, 5)

def selam():
    print("selam")

def selamGotur(isim):
    print("selam", isim)

selamGotur("Tugba")

# değer döndüren örnekler
def topla(a, b):
    return a + b

print(topla(3, 5))

def kareal(a):
    return a * a

sonuc = kareal(4)
print("karesi {}: ".format(sonuc))
print("karesi ", kareal(8))

# küçük örnekler
def cikar(x, y):
    print("sonuc :", x - y)
    return x - y

def kareal2(a):
    return a * a

cikar(10, 3)
kareal2(6)
cikar(5, 5)

# fonksiyon bileşimi ve liste üreteci
def ceyrek(x):
    return x / 4

def kupal(x):
    return x * x * x

print(kupal(3))
print(ceyrek(4))
print(kupal(ceyrek(12)))
print(kupal(ceyrek(20)))

liste1 = [1, 2, 3, 4, 5]
liste2 = [i * 2 for i in liste1]
print(liste2)

# lambda kısa örnek
kare = lambda x: x * x
print(kare(7))

# değişken adları
isim = "Tugba"
password = "Tugba"   # 'pass' anahtar kelimedir, kullanmayın.

# modüller
import math, time, random

print(math.pow(2, 2))
print(2 ** 2)
# cos/sin dereceyi radyana çevirerek
print(math.cos(math.radians(60)))
print(math.sin(math.radians(60)))
print(math.sqrt(4))

# basit tahmin oyunu (5 hak)
def tahmin_oyunu():
    rastgele = random.randint(1, 100)
    hak = 5
    print("1-100 arası sayı tuttum. Hakkın:", hak)

    while True:
        try:
            tahmin = int(input("Tahmin: "))
        except ValueError:
            print("Sayı gir.")
            continue

        if tahmin == rastgele:
            print("Doğru! sayı:", rastgele)
            break
        elif tahmin < rastgele:
            print("büyült")
        else:
            print("küçült")

        hak -= 1
        if hak <= 0:
            print("Hak bitti. sayı:", rastgele)
            break
        print("kalan hak:", hak)

# oyunu çalıştırmak istersen aşağıdakini aç:
# tahmin_oyunu()
