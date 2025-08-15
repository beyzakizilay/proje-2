Dosya_Adı="Liste.txt" 
def arac_ara():
    print("\nARAÇ ARAMA")
    anahtar=input("Plaka veya sahibi adı girin: ").lower()
    bulundu=False
    with open (Dosya_Adı,"r") as dosya:
        for satir in dosya:
            if anahtar in satir.lower():
                print("Bulundu: ",satir.strip())
                bulundu=True
    if not bulundu:
        print("Kayıt bulunamadı...")