"""M10 - Doğrusal (sıralı) arama.

Liste baştan sona tek tek gezilir; aranan değer bulunursa indeksi, bulunmazsa -1 döndürülür.
Liste sıralı olmak zorunda değildir.
"""


def dogrusal_ara(liste: list[int], hedef: int) -> int:
    """`hedef` değerinin listedeki ilk indeksini döndürür; yoksa -1 döndürür.

    Liste değiştirilmez.
    """
    for i in range(len(liste)):
        if liste[i] == hedef:
            return i  # bulduk: aramayı hemen bitir
    return -1  # döngü bitti, hiçbir eleman eşit değildi


def dogrusal_ara_sayarak(liste: list[int], hedef: int) -> tuple[int, int]:
    """`dogrusal_ara` ile aynı işi yapar, ek olarak yapılan karşılaştırma sayısını da döndürür.

    Dönüş değeri: (indeks, karsilastirma_sayisi). Bulunamazsa indeks -1'dir.
    """
    karsilastirma = 0
    for i in range(len(liste)):
        karsilastirma += 1  # liste[i] == hedef sorusunu bir kez sorduk
        if liste[i] == hedef:
            return i, karsilastirma
    return -1, karsilastirma


if __name__ == "__main__":
    notlar = [72, 45, 90, 38, 66, 90, 51]
    aranan = int(input("Hangi notu arayalım? "))
    indeks, adim = dogrusal_ara_sayarak(notlar, aranan)
    if indeks == -1:
        print(f"{aranan} listede yok ({adim} karşılaştırma yapıldı).")
    else:
        print(f"{aranan}, {indeks}. indekste bulundu ({adim} karşılaştırma yapıldı).")
