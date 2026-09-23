"""M12 - Vaka 1: 1'den n'ye kadar olan sayıların toplamı (döngü ve Gauss formülü)."""

import time


def toplam_dongu(n: int) -> int:
    """1 + 2 + ... + n toplamını tek tek ekleyerek bulur. Yaklaşık n adım: O(n)."""
    toplam = 0
    for i in range(1, n + 1):
        toplam = toplam + i
    return toplam


def toplam_gauss(n: int) -> int:
    """Aynı toplamı n * (n + 1) / 2 formülüyle bulur. n ne olursa olsun birkaç adım: O(1)."""
    if n < 1:
        return 0
    return n * (n + 1) // 2  # n veya n + 1 çift olduğu için bölme her zaman tam çıkar


if __name__ == "__main__":
    # Basit zamanlama deneyi (bkz. M12 §4). print() ölçümün dışında tutulur.
    for boyut in [1_000, 100_000, 1_000_000]:
        baslangic = time.perf_counter()
        sonuc_dongu = toplam_dongu(boyut)
        sure_dongu = time.perf_counter() - baslangic

        baslangic = time.perf_counter()
        sonuc_gauss = toplam_gauss(boyut)
        sure_gauss = time.perf_counter() - baslangic

        assert sonuc_dongu == sonuc_gauss
        print(f"n={boyut:>9}: döngü {sure_dongu:.6f} sn, Gauss {sure_gauss:.6f} sn")
