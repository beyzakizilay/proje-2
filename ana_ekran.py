def anamenu():
     while True:
        print("╔══════════════════════════════════╗")
        print("║     ARAÇ MUAYENE TAKİP SİSTEMİ   ║")
        print("║                                  ║")
        print("║  1-Yeni Araç Kaydı Ekle          ║")
        print("║  2-Araç Listesini Göster         ║")
        print("║  3-Araç Ara                      ║")
        print("║  4-Araç Kaydını Sil              ║")
        print("║  5-Araç Bilgilerini Güncelle     ║")
        print("║  6-Muayene Sonucu Ekle/Güncelle  ║")
        print("║  7-Yaklaşan Muayeneleri Göster   ║")
        print("║  8-Araç Sahibi Notları           ║")
        print("║  9-Çıkış                         ║")
        print("║     Tercihiniz Nedir?            ║")
        print("╚══════════════════════════════════╝")

        secim = input("Seçiminiz nedir: ")
        if secim=="1":
            import moduller.yeni_arac_kaydi_ekle
            moduller.yeni_arac_kaydı_ekle.yeni_arac_ekle()

        elif secim == "10":
            print("Çıkış Yaptınız...")
            break

        else:
            print("Hatalı Tuşlama Yaptınız, 1-10 arasında bir seçim yapınız...")    
anamenu()