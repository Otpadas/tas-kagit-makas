
import random

print("Tuttuğum sayıyı tahmin et.")

while True:
    tutulan_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    print("\n1 ile 100 arasinda bir sayı tuttum.")

    while True:
        tahmin = int(input("Tahminin: "))
        tahmin_sayisi += 1

        if tahmin < tutulan_sayi:
            print("Daha büyük bir sayı gir.")

        elif tahmin > tutulan_sayi:
            print("Daha küçük bir sayı gir.")

        else:
            print("Tebrikler!")
            print("Deneme sayin:", tahmin_sayisi)
            break

    tekrar = input("Tekrar oynamak istiyor musun? (e/h): ").lower()

    if tekrar != "e":
        print("Baştan başlayalım.")
        break
