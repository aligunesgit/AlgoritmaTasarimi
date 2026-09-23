"""M7 - Tek yönlü (if) ve iki yönlü (if-else) seçim: öğrenci indirimi ve kargo ücreti."""

UCRETSIZ_KARGO_ESIGI = 500
KARGO_UCRETI = 49.90
INDIRIM_ORANI = 0.10


def kargo_ucreti(sepet_tutari: float) -> float:
    """Sepet tutarı eşik ve üzerindeyse 0, değilse sabit kargo ücretini döndürür."""
    if sepet_tutari >= UCRETSIZ_KARGO_ESIGI:
        return 0
    else:
        return KARGO_UCRETI


def odenecek_tutar(sepet_tutari: float, ogrenci_mi: bool) -> float:
    """Öğrenci indirimi ve kargo dahil ödenecek tutarı kuruşa yuvarlayarak döndürür.

    Kargo eşiği, indirimden ÖNCEKİ sepet tutarına göre uygulanır.
    """
    tutar = sepet_tutari
    if ogrenci_mi:  # tek yönlü seçim: öğrenci değilse hiçbir şey yapılmaz
        tutar = tutar - tutar * INDIRIM_ORANI
    tutar = tutar + kargo_ucreti(sepet_tutari)
    return round(tutar, 2)


if __name__ == "__main__":
    sepet = float(input("Sepet tutarı (TL): "))
    cevap = input("Öğrenci misiniz? (e/h): ")
    print(f"Ödenecek tutar: {odenecek_tutar(sepet, cevap == 'e')} TL")
