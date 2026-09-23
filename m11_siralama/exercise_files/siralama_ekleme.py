"""M11 - Ekleme sıralaması (insertion sort).

Listenin solunda sıralı bir bölüm tutulur. Sıradaki eleman (anahtar) alınır, kendisinden büyük
elemanlar birer sağa kaydırılır ve anahtar açılan boşluğa yerleştirilir. Elimizdeki iskambil
kartlarını dizerken yaptığımız şeyin aynısıdır.
"""


def ekleme_sirala(liste: list[int]) -> list[int]:
    """Listenin küçükten büyüğe sıralanmış bir KOPYASINI döndürür.

    Girdi listesi değiştirilmez (yerinde sıralama yapılmaz).
    """
    sonuc = liste.copy()
    for i in range(1, len(sonuc)):
        anahtar = sonuc[i]  # yerleştirilecek eleman
        j = i - 1
        while j >= 0 and sonuc[j] > anahtar:
            sonuc[j + 1] = sonuc[j]  # büyük elemanı bir sağa kaydır
            j = j - 1
        sonuc[j + 1] = anahtar  # açılan boşluğa yerleştir
    return sonuc


def ekleme_sirala_sayarak(liste: list[int]) -> tuple[list[int], int, int]:
    """`ekleme_sirala` ile aynı işi yapar; karşılaştırma ve kaydırma sayılarını da döndürür.

    Karşılaştırma: `sonuc[j] > anahtar` sorusunun kaç kez sorulduğu.
    Kaydırma: bir elemanın bir sağa taşınma sayısı (takasın karşılığı).
    Dönüş değeri: (sirali_kopya, karsilastirma_sayisi, kaydirma_sayisi). Girdi değiştirilmez.
    """
    sonuc = liste.copy()
    karsilastirma = 0
    kaydirma = 0
    for i in range(1, len(sonuc)):
        anahtar = sonuc[i]
        j = i - 1
        while j >= 0:
            karsilastirma += 1
            if sonuc[j] <= anahtar:
                break  # doğru yer bulundu
            sonuc[j + 1] = sonuc[j]
            kaydirma += 1
            j = j - 1
        sonuc[j + 1] = anahtar
    return sonuc, karsilastirma, kaydirma


if __name__ == "__main__":
    ornek = [5, 2, 9, 1, 6]
    sirali, k, t = ekleme_sirala_sayarak(ornek)
    print(f"{ornek} -> {sirali} ({k} karşılaştırma, {t} kaydırma)")
