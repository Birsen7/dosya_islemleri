import random

rastgele_sayi = [random.randint(1,100) for _ in range(10)]
print("Üretilen rastgele sayılar: ", rastgele_sayi)


with open("sayilar.txt", "w") as dosya:
       for sayi in rastgele_sayi:
              dosya.write(f"{sayi}\n")


with open("sayilar.txt", "r") as dosya:
       okunan_sayilar = [int(sayi.strip()) for sayi in dosya.readlines()]

print("Okunan Sayılar: ", okunan_sayilar)


toplam = sum(okunan_sayilar)
ortalama = toplam / len(okunan_sayilar)
en_buyuk = max(okunan_sayilar)
en_kucuk = min(okunan_sayilar)

print(f"Toplam: {toplam}, Ortalama: {ortalama}, En Büyük: {en_buyuk}, En Küçük: {en_kucuk}")


with open("sonuclar.txt", "w") as dosya:
       dosya.write(f"Toplam: {toplam}\n")
       dosya.write(f"Ortalama: {ortalama}\n")
       dosya.write(f"En Büyük: {en_buyuk}\n")
       dosya.write(f"En Küçük: {en_kucuk}\n")