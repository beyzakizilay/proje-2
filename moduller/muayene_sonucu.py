Dosya_Adı="araclar.txt"
def muayene():
    plaka = input("Plaka girin: ")
    satirlar = []
    bulundu = False
    with open(Dosya_Adı, "r") as dosya:
        for satir in dosya:
            veri = satir.strip().split(",")
            if veri[0] == plaka:
                print("Mevcut Bilgi:", satir.strip())
                sonuc = input("Muayene Sonucu (Geçti/Kaldı): ")
                veri[7] = sonuc
                satirlar.append(",".join(veri) + "\n")
                bulundu = True
            else:
                satirlar.append(satir)
    with open(Dosya_Adı, "w") as dosya:
        dosya.writelines(satirlar)
    print("Sonuç güncellendi." if bulundu else "Plaka bulunamadı.")
