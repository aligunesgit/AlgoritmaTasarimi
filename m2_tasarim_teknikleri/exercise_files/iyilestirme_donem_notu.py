"""M2 - Adım adım iyileştirme: dönem notu hesabının 3. seviye inceltmesi.

README §5'teki üç seviyeli inceltmenin son hâli burada Python'a çevrilmiştir.
Geçti/kaldı kararını M7'de ekleyeceğiz.
"""


def agirlikli_ortalama(vize: float, final: float, vize_agirlik: float = 0.4) -> float:
    """Vize ve finalin ağırlıklı ortalamasını bir ondalık basamağa yuvarlayarak döndürür."""
    final_agirlik = 1 - vize_agirlik
    return round(vize * vize_agirlik + final * final_agirlik, 1)


if __name__ == "__main__":
    vize_notu = float(input("Vize notu: "))
    final_notu = float(input("Final notu: "))
    print(f"Dönem notu: {agirlikli_ortalama(vize_notu, final_notu)}")
