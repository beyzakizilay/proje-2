Dosya_Adı="araclar.txt"
from datetime import datetime
def yaklasan_muayene():
    print("\n[Yaklaşan Muayeneler]")
    bugun = datetime.today()
    with open(Dosya_Adı, "r") as dosya:
        for satir in dosya:
            veri = satir.strip().split(",")
            try:
                tarih = datetime.strptime(veri[6], "%Y-%m-%d")
                kalan = (tarih - bugun).days
                if 0 <= kalan <= 7:
                    print(f"{veri[0]} - {veri[4]} ({veri[6]}) → {kalan} gün kaldı.")
            except:
                continue
