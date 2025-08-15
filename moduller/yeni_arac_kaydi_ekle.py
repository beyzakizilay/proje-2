import os
Dosya_Adı="Liste.txt"
def yeni_arac_ekle():
    print("\nARAÇ KAYIT")
    plaka=input("Plaka: ")
    marka=input("Marka: ")
    model=input("Model: ")
    yil=input("Yıl: ")
    sahip=input("Araç Sahibinin Adı: ")
    telefon=input("Telefon: ")
    muayene_tarihi=input("Muayene Tarihi (gg-aa-yyyy): ")
    sonuc="Bekliyor..."
    notlar=""
    satir=f"{plaka},{model},{yil},{sahip},{telefon},{muayene_tarihi},{sonuc},{notlar}\n"
    with open(Dosya_Adı,"a") as dosya:
        dosya.write(satir)
    print("Araç başarıyla kaydedildi.\n")
