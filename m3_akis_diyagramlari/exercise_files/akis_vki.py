"""M3 - Vücut kitle indeksi (VKİ): sıra ve seçim yapısı.

README §4'teki akış şemasının Python karşılığıdır. Karar yapısını (if/elif/else)
M7'de ayrıntılı göreceğiz. Fonksiyonları M1'deki gibi, test edilebilsin diye bir
kutuya koyuyoruz; ayrıntısı M9'da.
"""


def vki_hesapla(kilo: float, boy_m: float) -> float:
    """VKİ = kilo / boy²; sonucu bir ondalığa yuvarlar."""
    return round(kilo / (boy_m * boy_m), 1)


def vki_kategori(vki: float) -> str:
    """Dünya Sağlık Örgütü'nün yetişkinler için kullandığı sınıflara göre kategori döndürür."""
    if vki < 18.5:
        return "Zayıf"
    elif vki < 25:
        return "Normal"
    elif vki < 30:
        return "Fazla kilolu"
    else:
        return "Obez"


if __name__ == "__main__":
    kilo = float(input("Kilonuz (kg): "))
    boy = float(input("Boyunuz (m): "))
    deger = vki_hesapla(kilo, boy)
    print(f"VKİ: {deger} ({vki_kategori(deger)})")
