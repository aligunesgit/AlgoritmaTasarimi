"""M7 - Çok yönlü seçim (if-elif-else): puanı harf notuna çevirir.

Basitleştirilmiş ölçek: 90-100 AA, 75-89 BB, 60-74 CC, 50-59 DD, 0-49 FF.
"""


def harf_notu(puan: float) -> str:
    """0-100 arası puanı harf notuna çevirir; aralık dışı puanlar için "Geçersiz" döndürür."""
    if puan < 0 or puan > 100:
        return "Geçersiz"
    elif puan >= 90:  # en büyük eşikten başlıyoruz (bkz. M7 §4.1)
        return "AA"
    elif puan >= 75:
        return "BB"
    elif puan >= 60:
        return "CC"
    elif puan >= 50:
        return "DD"
    else:
        return "FF"


if __name__ == "__main__":
    girilen = float(input("Puanınız (0-100): "))
    print(f"Harf notunuz: {harf_notu(girilen)}")
