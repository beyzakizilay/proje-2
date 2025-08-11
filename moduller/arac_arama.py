Dosya_Adı="araclar.txt" 
def arac_ara():
    anahtar=input("Plaka veya sahibi adı girin: ").lower()
    bulundu=False
    with open (Dosya_Adı,"r") as dosya:
        for satir in dosya:
            if anahtar in satir.lower():
                print("Bulundu: ",satir.strip())
                bulundu=True
    if not bulundu:
        print("Kayıt bulunamadı...")