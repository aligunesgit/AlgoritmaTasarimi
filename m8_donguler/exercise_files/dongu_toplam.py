"""M8 - Sayaç kontrollü ve koşul kontrollü iki toplama döngüsü."""


def toplam_1den_n(n: int) -> int:
    """1'den n'e kadar olan tam sayıların toplamını döndürür (for + range).

    n 1'den küçükse döngü hiç çalışmaz ve sonuç 0 olur.
    """
    toplam = 0  # toplayıcı: başlangıç değeri 0
    for i in range(1, n + 1):  # n + 1 yazmazsak n dahil edilmez
        toplam = toplam + i
    return toplam


def rakamlar_toplami(n: int) -> int:
    """Negatif olmayan bir tam sayının rakamlarının toplamını döndürür (while).

    Kaç tur döneceğimizi baştan bilmiyoruz; sayı 0 olana kadar son rakamı koparırız.
    """
    toplam = 0
    while n > 0:
        son_rakam = n % 10  # 472 % 10 -> 2
        toplam = toplam + son_rakam
        n = n // 10  # 472 // 10 -> 47 (bitiş koşuluna yaklaştıran adım)
    return toplam


if __name__ == "__main__":
    sayi = int(input("Bir pozitif tam sayı girin: "))
    print(f"1'den {sayi}'e kadar toplam: {toplam_1den_n(sayi)}")
    print(f"{sayi} sayısının rakamları toplamı: {rakamlar_toplami(sayi)}")
