Dosya_Adı="araclar.txt"

def sahip_notlari():
    plaka = input("Not eklenecek plakayı girin: ")
    satirlar = []
    bulundu = False
    with open(Dosya_Adı, "r") as dosya:
        for satir in dosya:
            veri = satir.strip().split(",")
            if veri[0] == plaka:
                print("Mevcut Not:", veri[8])
                yeni_not = input("Yeni Not: ")
                veri[8] = yeni_not
                satirlar.append(",".join(veri) + "\n")
                bulundu = True
            else:
                satirlar.append(satir)
    with open(Dosya_Adı, "w") as dosya:
        dosya.writelines(satirlar)
    print("Not eklendi." if bulundu else "Plaka bulunamadı.")
