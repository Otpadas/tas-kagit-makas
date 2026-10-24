import random

secenekler = ["taş", "kağıt", "makas"]

bilgisayar = random.choice(secenekler)

oyuncu = input("Taş, kağıt veya makas: ").lower()

print("Benim seçimim:", bilgisayar)

if oyuncu not in secenekler:
    print("Yanlış yazmış olabilirsin :)")

elif oyuncu == bilgisayar:
    print("Berabere")

elif oyuncu == "taş" and bilgisayar == "makas":
    print("Kazandın")

elif oyuncu == "kağıt" and bilgisayar == "taş":
    print("Kazandın")

elif oyuncu == "makas" and bilgisayar == "kağıt":
    print("Kazandın")

else:
    print("Ben kazandım.")