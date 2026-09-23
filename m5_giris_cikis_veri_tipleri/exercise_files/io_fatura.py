"""M5 - Basit fatura: adet ve birim fiyattan ara toplam, KDV ve genel toplam."""

KDV_ORANI = 0.20  # Genel KDV oranı (%20). Sabitleri M6'da ayrıntılı göreceğiz.


def kdv_tutari(ara_toplam: float, oran: float) -> float:
    """Ara toplamın KDV tutarını 2 ondalık basamağa yuvarlanmış olarak döndürür."""
    return round(ara_toplam * oran, 2)


def fatura_metni(urun: str, adet: int, birim_fiyat: float, oran: float) -> str:
    """Hizalanmış, dört satırlık bir fatura metni döndürür."""
    ara_toplam = adet * birim_fiyat
    kdv = kdv_tutari(ara_toplam, oran)
    genel_toplam = ara_toplam + kdv
    kdv_etiketi = f"KDV (%{oran * 100:.0f})"  # ör. "KDV (%20)"
    # :<12 → 12 karakterlik alana sola yasla, :>10.2f → 10 karakterlik alana sağa yasla, 2 basamak
    return (
        f"{'Ürün':<12}{urun:>13}\n"
        f"{'Ara toplam':<12}{ara_toplam:>10.2f} TL\n"
        f"{kdv_etiketi:<12}{kdv:>10.2f} TL\n"
        f"{'Toplam':<12}{genel_toplam:>10.2f} TL"
    )


if __name__ == "__main__":
    urun_adi = input("Ürün adı: ")
    urun_adedi = int(input("Adet: "))
    fiyat = float(input("Birim fiyat (TL): "))
    print(fatura_metni(urun_adi, urun_adedi, fiyat, KDV_ORANI))
