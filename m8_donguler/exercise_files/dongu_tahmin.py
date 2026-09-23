"""M8 - Sayı tahmin oyunu: koşul kontrollü döngü ve break."""

import random


def tahmin_degerlendir(tahmin: int, hedef: int) -> str:
    """Tahmini hedefle karşılaştırıp oyuncuya verilecek ipucunu döndürür."""
    if tahmin < hedef:
        return "Daha büyük bir sayı deneyin."
    elif tahmin > hedef:
        return "Daha küçük bir sayı deneyin."
    else:
        return "Doğru!"


def deneme_sayisi(hedef: int, tahminler: list[int]) -> int:
    """Tahminler sırayla yapıldığında hedefin kaçıncı denemede bulunduğunu döndürür.

    Hedef hiç bulunamazsa -1 döndürür.
    """
    deneme = 0
    bulundu = False
    for tahmin in tahminler:
        deneme = deneme + 1
        if tahmin == hedef:
            bulundu = True
            break  # bulduk; kalan tahminlere bakmaya gerek yok
    if bulundu:
        return deneme
    return -1


if __name__ == "__main__":
    hedef = random.randint(1, 100)  # 1 ile 100 arasında (ikisi dahil) rastgele tam sayı
    deneme = 0
    print("1 ile 100 arasında bir sayı tuttum.")
    while True:
        tahmin = int(input("Tahmininiz: "))
        deneme = deneme + 1
        ipucu = tahmin_degerlendir(tahmin, hedef)
        print(ipucu)
        if tahmin == hedef:
            break
    print(f"{deneme} denemede buldunuz.")
