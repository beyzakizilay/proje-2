Dosya_Adı = "Liste.txt"
def guncelleme():
    plaka = input("Güncellenecek plakayı girin: ").upper()
    bulundu = False
    yeni_liste = []
    try:
        with open(Dosya_Adı, "r", encoding="utf-8") as dosya:
            okunan=dosya.read()
            for satir in okunan:
                veri = satir.strip().split(",")
                if plaka == veri[0].upper():
                    bulundu = True
                    print("Mevcut kayıt:", satir.strip())
                    marka = input("Yeni Marka: ")
                    model = input("Yeni Model: ")
                    yil = input("Yeni Yıl: ")
                    sahip = input("Yeni Sahip: ")
                    telefon = input("Yeni Telefon: ")
                    muayene = input("Yeni Muayene Tarihi (GG-AA-YYYY): ")
                    durum = input("Yeni Durum: ")
                    satir = f"{plaka},{marka},{model},{yil},{sahip},{telefon},{muayene},{durum}\n"
                    print("Güncellenen kayıt:", satir.strip())

                yeni_liste.append(satir)
        if not bulundu:
            print("Güncellenecek kayıt bulunamadı!")
        else:
            with open(Dosya_Adı, "w", encoding="utf-8") as dosya:
                dosya.writelines(yeni_liste)
            print("Güncelleme tamamlandı!")
    except FileNotFoundError:
        print(f"{Dosya_Adı} dosyası bulunamadı!")


