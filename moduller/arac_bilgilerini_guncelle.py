Dosya_Adı="araclar.txt"
def guncelleme():
    plaka=input("Güncellenecek plakayı girin: ")
    satirlar=[]
    bulundu=False
    with open(Dosya_Adı,"r") as dosya:
        for satir in dosya:
            if satir.startswith(plaka):
                print("Eski kayıt:",satir.strip())
                yeni_tel=input("Yeni telefon: ")
                yeni_satir=satir.strip().split(",")
                yeni_satir[5]=yeni_tel
                satirlar.append(",".join(yeni_satir)+"\n")
                bulundu=True
            else:
                satirlar.append(satir)
    with open (Dosya_Adı,"w")as dosya:
        print(f"{satirlar}")
    print("Güncellendi.")               