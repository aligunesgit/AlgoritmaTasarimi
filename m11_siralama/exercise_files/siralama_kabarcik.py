"""M11 - Kabarcık sıralama (bubble sort), erken çıkış bayrağıyla.

Yan yana duran iki eleman yanlış sıradaysa yer değiştirilir. Her geçişin sonunda en büyük eleman
listenin sonuna "kabarcık gibi" yükselir. Bir geçişte hiç takas olmazsa liste sıralıdır ve durulur.
"""


def kabarcik_sirala(liste: list[int]) -> list[int]:
    """Listenin küçükten büyüğe sıralanmış bir KOPYASINI döndürür.

    Girdi listesi değiştirilmez (yerinde sıralama yapılmaz).
    """
    sonuc = liste.copy()
    n = len(sonuc)
    for gecis in range(n - 1):
        takas_oldu = False  # bayrak: bu geçişte en az bir takas yapıldı mı?
        for j in range(n - 1 - gecis):  # sondaki gecis kadar eleman zaten yerinde
            if sonuc[j] > sonuc[j + 1]:
                sonuc[j], sonuc[j + 1] = sonuc[j + 1], sonuc[j]
                takas_oldu = True
        if not takas_oldu:
            break  # erken çıkış: liste zaten sıralı
    return sonuc


def kabarcik_sirala_sayarak(liste: list[int]) -> tuple[list[int], int, int]:
    """`kabarcik_sirala` ile aynı işi yapar; karşılaştırma ve takas sayılarını da döndürür.

    Dönüş değeri: (sirali_kopya, karsilastirma_sayisi, takas_sayisi). Girdi değiştirilmez.
    """
    sonuc = liste.copy()
    n = len(sonuc)
    karsilastirma = 0
    takas = 0
    for gecis in range(n - 1):
        takas_oldu = False
        for j in range(n - 1 - gecis):
            karsilastirma += 1
            if sonuc[j] > sonuc[j + 1]:
                sonuc[j], sonuc[j + 1] = sonuc[j + 1], sonuc[j]
                takas += 1
                takas_oldu = True
        if not takas_oldu:
            break
    return sonuc, karsilastirma, takas


if __name__ == "__main__":
    ornek = [5, 2, 9, 1, 6]
    sirali, k, t = kabarcik_sirala_sayarak(ornek)
    print(f"{ornek} -> {sirali} ({k} karşılaştırma, {t} takas)")
