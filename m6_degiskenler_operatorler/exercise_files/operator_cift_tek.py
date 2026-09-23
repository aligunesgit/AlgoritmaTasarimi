"""M6 - Mod (%) operatörüyle çift/tek ve kat kontrolü."""


def cift_mi(sayi: int) -> bool:
    """Sayı çiftse True, tekse False döndürür."""
    return sayi % 2 == 0


def kati_mi(sayi: int, bolen: int) -> bool:
    """Sayı, bolen'in tam katıysa True döndürür (bolen sıfır olmamalı)."""
    return sayi % bolen == 0


if __name__ == "__main__":
    girilen = int(input("Bir tam sayı girin: "))
    print(f"{girilen} çift mi? {cift_mi(girilen)}")
    print(f"{girilen} 5'in katı mı? {kati_mi(girilen, 5)}")
