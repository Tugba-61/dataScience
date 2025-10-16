# Faktöriyel Hesaplama ve Açılımını Yazdırma

def faktoriyel(n):
    carpim = 1
    acilim = ""  # açılımı tutmak için
    for i in range(n, 0, -1):
        carpim *= i
        acilim += str(i)
        if i > 1:
            acilim += " x "
    print(f"{n}! = {acilim} = {carpim}")
    return carpim

# Kullanım
sayi = int(input("Bir sayı giriniz: "))
faktoriyel(sayi)
