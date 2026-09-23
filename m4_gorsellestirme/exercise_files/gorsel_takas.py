"""M4 - İki değişkenin değerini takas etme (Python Tutor ile izlemek için)."""


def takas(a: int, b: int) -> tuple[int, int]:
    """a ile b'nin yerini değiştirir ve (yeni_a, yeni_b) çiftini döndürür.

    Üçüncü bir "geçici" değişken kullanıyoruz; böylece her adımda hangi
    değerin nerede durduğunu Python Tutor'da ya da iz tablosunda görebiliriz.
    """
    gecici = a  # 1. a'nın değerini kaybetmemek için sakla
    a = b  # 2. a artık b'nin değerini tutuyor
    b = gecici  # 3. b, saklanan eski a değerini alıyor
    return a, b


if __name__ == "__main__":
    x = 3
    y = 7
    x, y = takas(x, y)
    print("x =", x, "y =", y)
