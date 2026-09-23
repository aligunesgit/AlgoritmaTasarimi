"""M2 - Sayı tahmin oyunu: kaba kuvvet ile yarıya bölmenin karşılaştırılması.

Bu dosyada karar (if) ve döngü (while) kullanıyoruz. Bunları M7 ve M8'de ayrıntılı
göreceğiz; şimdilik kodu sözde kodla yan yana okumanız yeterli.
"""


def _aralik_kontrol(gizli: int, alt: int, ust: int) -> None:
    """Gizli sayı aralığın dışındaysa hata verir."""
    if not alt <= gizli <= ust:
        raise ValueError(f"Gizli sayı {alt} ile {ust} arasında olmalı.")


def kaba_kuvvet_tahmin_sayisi(gizli: int, alt: int = 1, ust: int = 100) -> int:
    """Sayıları alttan başlayarak sırayla dener; kaçıncı tahminde bulduğunu döndürür."""
    _aralik_kontrol(gizli, alt, ust)
    tahmin = alt
    sayac = 1
    while tahmin != gizli:
        tahmin = tahmin + 1
        sayac = sayac + 1
    return sayac


def yariya_bolme_tahmin_sayisi(gizli: int, alt: int = 1, ust: int = 100) -> int:
    """Her seferinde kalan aralığın ortasını dener; kaçıncı tahminde bulduğunu döndürür."""
    _aralik_kontrol(gizli, alt, ust)
    sayac = 0
    while True:
        orta = (alt + ust) // 2  # ortadaki sayı (aşağı yuvarlanır)
        sayac = sayac + 1
        if orta == gizli:
            return sayac
        if orta < gizli:  # "daha büyük" cevabı: alt yarıyı at
            alt = orta + 1
        else:  # "daha küçük" cevabı: üst yarıyı at
            ust = orta - 1


if __name__ == "__main__":
    sayi = int(input("1 ile 100 arasında gizli bir sayı girin: "))
    print(f"Kaba kuvvet  : {kaba_kuvvet_tahmin_sayisi(sayi)} tahmin")
    print(f"Yarıya bölme : {yariya_bolme_tahmin_sayisi(sayi)} tahmin")
