Dosya_Adı="Liste.txt"
def kayit_sil():
    print("\nARAÇ KAYDI SİLME")
    plaka=input("Silinecek aracın palaksı: ")
    satirlar=[]
    bulundu=False
    with open(Dosya_Adı, "r") as dosya:
        for satir in dosya:
            if not satir.startswith(plaka):
                satirlar.append(satir)
            else:
                bulundu=True
    with open(Dosya_Adı,"w") as dosya:
        print(f"{satirlar}")
    print("Silme işlemi tamamlandı.")