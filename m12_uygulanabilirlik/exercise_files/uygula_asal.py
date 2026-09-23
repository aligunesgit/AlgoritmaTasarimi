"""M12 - Vaka 4: Asal sayı testi (tüm bölenler ve karekök sınırı)."""


def asal_mi_tum(n: int) -> bool:
    """2'den n - 1'e kadar tüm sayıları bölen olarak dener. En kötü yaklaşık n adım: O(n)."""
    if n < 2:
        return False
    for bolen in range(2, n):  # noqa: SIM110 (açık döngü, öğretim amaçlı)
        if n % bolen == 0:
            return False
    return True


def asal_mi_karekok(n: int) -> bool:
    """Yalnızca bolen * bolen ≤ n olan bölenleri dener. En kötü yaklaşık √n adım: O(√n)."""
    if n < 2:
        return False
    bolen = 2
    while bolen * bolen <= n:
        if n % bolen == 0:
            return False
        bolen = bolen + 1
    return True


def deneme_sayisi_tum(n: int) -> int:
    """asal_mi_tum fonksiyonunun kaç bölen denediğini sayar."""
    deneme = 0
    for bolen in range(2, n):
        deneme = deneme + 1
        if n % bolen == 0:
            break
    return deneme


def deneme_sayisi_karekok(n: int) -> int:
    """asal_mi_karekok fonksiyonunun kaç bölen denediğini sayar."""
    deneme = 0
    bolen = 2
    while bolen * bolen <= n:
        deneme = deneme + 1
        if n % bolen == 0:
            break
        bolen = bolen + 1
    return deneme


if __name__ == "__main__":
    sayi = int(input("Bir tam sayı girin: "))
    print(f"Asal mı? {asal_mi_karekok(sayi)}")
    print(f"Tüm bölenler yöntemi {deneme_sayisi_tum(sayi)} deneme yaptı.")
    print(f"Karekök yöntemi {deneme_sayisi_karekok(sayi)} deneme yaptı.")
