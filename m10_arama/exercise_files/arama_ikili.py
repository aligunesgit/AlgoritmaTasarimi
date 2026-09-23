"""M10 - İkili arama (binary search), iteratif sürüm.

ÖN KOŞUL: liste küçükten büyüğe sıralı olmalıdır. Her adımda aralığın ortasındaki elemana
bakılır ve aralığın yarısı atılır.
"""


def ikili_ara(liste: list[int], hedef: int) -> int:
    """Sıralı `liste` içinde `hedef` değerini arar; bulunursa bir indeksini, yoksa -1 döndürür.

    Liste sıralı değilse sonuç güvenilir değildir. Liste değiştirilmez.
    Tekrarlı elemanlarda döndürülen indeks, eşit elemanlardan herhangi biri olabilir.
    """
    sol = 0
    sag = len(liste) - 1
    while sol <= sag:  # aralıkta en az bir eleman kaldığı sürece
        orta = (sol + sag) // 2  # tam sayı bölmesi: indeks tam sayı olmalı
        if liste[orta] == hedef:
            return orta
        elif liste[orta] < hedef:
            sol = orta + 1  # hedef sağ yarıda: orta dahil sol yarıyı at
        else:
            sag = orta - 1  # hedef sol yarıda: orta dahil sağ yarıyı at
    return -1


def ikili_ara_sayarak(liste: list[int], hedef: int) -> tuple[int, int]:
    """`ikili_ara` ile aynı işi yapar, ek olarak kaç kez orta elemana bakıldığını döndürür.

    Her tur (orta elemanla bir kıyaslama) bir karşılaştırma sayılır.
    Dönüş değeri: (indeks, karsilastirma_sayisi).
    """
    sol = 0
    sag = len(liste) - 1
    karsilastirma = 0
    while sol <= sag:
        orta = (sol + sag) // 2
        karsilastirma += 1
        if liste[orta] == hedef:
            return orta, karsilastirma
        elif liste[orta] < hedef:
            sol = orta + 1
        else:
            sag = orta - 1
    return -1, karsilastirma


if __name__ == "__main__":
    sayilar = list(range(1, 1001))  # 1, 2, ..., 1000 (sıralı)
    aranan = int(input("1 ile 1000 arasında bir sayı: "))
    indeks, adim = ikili_ara_sayarak(sayilar, aranan)
    print(f"Sonuç indeksi: {indeks}, karşılaştırma sayısı: {adim}")
