"""M3 - 1'den n'ye kadar sayıların toplamı: tekrar yapısı.

README §5'teki iz tablosu bu fonksiyonun n = 4 için adım adım çalışmasıdır.
Döngüyü (while) M8'de ayrıntılı göreceğiz.
"""


def ilk_n_toplam(n: int) -> int:
    """1 + 2 + ... + n toplamını döndürür. n < 1 ise toplam 0'dır."""
    toplam = 0
    i = 1
    while i <= n:
        toplam = toplam + i
        i = i + 1
    return toplam


if __name__ == "__main__":
    sayi = int(input("n: "))
    print(f"Toplam: {ilk_n_toplam(sayi)}")
