"""M12 - Vaka 2: Bir listede tekrar eden eleman var mı? Üç farklı algoritma."""


def tekrar_var_ic_ice(liste: list[int]) -> bool:
    """Her elemanı kendinden sonraki tüm elemanlarla karşılaştırır. Yaklaşık n²/2 adım: O(n²)."""
    n = len(liste)
    for i in range(n):
        for j in range(i + 1, n):
            if liste[i] == liste[j]:
                return True
    return False


def tekrar_var_sirali(liste: list[int]) -> bool:
    """Listenin sıralı bir kopyasını alır; tekrar eden elemanlar artık yan yanadır.

    Sıralama yaklaşık n log n, ardından tek geçiş n adım sürer: toplamda O(n log n).
    """
    sirali = sorted(liste)  # Orijinal liste değişmez
    for i in range(len(sirali) - 1):  # noqa: SIM110 (açık döngü, öğretim amaçlı)
        if sirali[i] == sirali[i + 1]:
            return True
    return False


def tekrar_var_kume(liste: list[int]) -> bool:
    """Görülen elemanları bir kümede (set) tutar. Ortalama n adım: O(n), ama ek bellek ister."""
    gorulenler: set[int] = set()
    for eleman in liste:
        if eleman in gorulenler:
            return True
        gorulenler.add(eleman)
    return False


if __name__ == "__main__":
    metin = input("Sayıları boşlukla ayırarak girin: ")
    sayilar = [int(parca) for parca in metin.split()]
    print("İç içe döngü :", tekrar_var_ic_ice(sayilar))
    print("Önce sırala  :", tekrar_var_sirali(sayilar))
    print("Küme (set)   :", tekrar_var_kume(sayilar))
