"""M3 - Üç sayının en büyüğü: iç içe olmayan ardışık kararlar.

README §6'daki sözde kod ↔ akış şeması dönüşüm örneğinin Python karşılığıdır.
"""


def en_buyuk_uc(a: float, b: float, c: float) -> float:
    """Üç sayının en büyüğünü döndürür (hazır max() kullanmadan)."""
    en_buyuk = a
    if b > en_buyuk:
        en_buyuk = b
    if c > en_buyuk:
        en_buyuk = c
    return en_buyuk


if __name__ == "__main__":
    x = float(input("1. sayı: "))
    y = float(input("2. sayı: "))
    z = float(input("3. sayı: "))
    print(f"En büyük: {en_buyuk_uc(x, y, z)}")
