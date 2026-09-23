"""M11 - Seçmeli sıralama (selection sort).

Her geçişte sıralanmamış kısmın en küçük elemanı bulunur ve o kısmın başına getirilir.
"""


def secmeli_sirala(liste: list[int]) -> list[int]:
    """Listenin küçükten büyüğe sıralanmış bir KOPYASINI döndürür.

    Girdi listesi değiştirilmez (yerinde sıralama yapılmaz).
    """
    sonuc = liste.copy()  # orijinali korumak için kopya üzerinde çalış
    n = len(sonuc)
    for i in range(n - 1):
        en_kucuk = i  # sıralanmamış kısmın ilk elemanını en küçük varsay
        for j in range(i + 1, n):
            if sonuc[j] < sonuc[en_kucuk]:
                en_kucuk = j
        if en_kucuk != i:
            sonuc[i], sonuc[en_kucuk] = sonuc[en_kucuk], sonuc[i]  # takas
    return sonuc


def secmeli_sirala_sayarak(liste: list[int]) -> tuple[list[int], int, int]:
    """`secmeli_sirala` ile aynı işi yapar; karşılaştırma ve takas sayılarını da döndürür.

    Dönüş değeri: (sirali_kopya, karsilastirma_sayisi, takas_sayisi). Girdi değiştirilmez.
    """
    sonuc = liste.copy()
    n = len(sonuc)
    karsilastirma = 0
    takas = 0
    for i in range(n - 1):
        en_kucuk = i
        for j in range(i + 1, n):
            karsilastirma += 1
            if sonuc[j] < sonuc[en_kucuk]:
                en_kucuk = j
        if en_kucuk != i:
            sonuc[i], sonuc[en_kucuk] = sonuc[en_kucuk], sonuc[i]
            takas += 1
    return sonuc, karsilastirma, takas


if __name__ == "__main__":
    ornek = [5, 2, 9, 1, 6]
    sirali, k, t = secmeli_sirala_sayarak(ornek)
    print(f"{ornek} -> {sirali} ({k} karşılaştırma, {t} takas)")
