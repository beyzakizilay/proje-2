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
            moduller.yeni_arac_kaydi_ekle.yeni_arac_ekle()

        elif secim=="2":
            import moduller.arac_listesi_goster
            moduller.arac_listesi_goster.arac_listesi()

        elif secim=="3":
            import moduller.arac_arama
            moduller.arac_arama.arac_ara()

        elif secim=="4":
            import moduller.arac_kaydi_sil
            moduller.arac_kaydi_sil.kayit_sil()

        elif secim=="5":
            import moduller.arac_bilgilerini_guncelle
            moduller.arac_bilgilerini_guncelle.guncelleme()

        elif secim=="6":
            import moduller.muayene_sonucu
            moduller.muayene_sonucu.muayene()  

        elif secim=="7":
            import moduller.yaklasan_muayene_goster
            moduller.yaklasan_muayene_goster.yaklasan_muayene()  

        elif secim=="8":
            import moduller.arac_sahibi_notlari
            moduller.arac_sahibi_notlari.sahip_notlari()   
        
        elif secim == "9":
            print("Çıkış Yaptınız...")
            break

        else:
            print("Hatalı Tuşlama Yaptınız, 1-10 arasında bir seçim yapınız...")    
anamenu()