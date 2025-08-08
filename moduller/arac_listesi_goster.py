import os
Dosya_Adı = "Liste.txt"
def arac_listesi():
    print("\nKAYITLI ARAÇLAR")
    try:
        with open(Dosya_Adı, "r") as dosya:
            for sira, satir in enumerate(dosya, 1):
                veri = satir.strip().split(",")
                print(sira, veri)
    except FileNotFoundError:
        print("Liste.txt dosyası bulunamadı!")
