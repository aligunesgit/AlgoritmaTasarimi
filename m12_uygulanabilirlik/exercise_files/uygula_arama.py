"""M12 - Vaka 3: Doğrusal arama ile sırala + ikili arama karşılaştırması."""


def dogrusal_ara(liste: list[int], hedef: int) -> int:
    """Hedefin indeksini baştan sona tarayarak bulur; yoksa -1 döndürür. En kötü n adım: O(n)."""
    for i in range(len(liste)):
        if liste[i] == hedef:
            return i
    return -1


def ikili_ara(sirali: list[int], hedef: int) -> int:
    """SIRALI listede hedefin indeksini bulur; yoksa -1 döndürür. En kötü yaklaşık log2(n) adım: O(log n)."""
    alt = 0
    ust = len(sirali) - 1
    while alt <= ust:
        orta = (alt + ust) // 2
        if sirali[orta] == hedef:
            return orta
        elif sirali[orta] < hedef:
            alt = orta + 1
        else:
            ust = orta - 1
    return -1


def dogrusal_adim(liste: list[int], hedef: int) -> int:
    """Doğrusal aramanın kaç karşılaştırma yaptığını sayar."""
    adim = 0
    for eleman in liste:
        adim = adim + 1
        if eleman == hedef:
            break
    return adim


def ikili_adim(sirali: list[int], hedef: int) -> int:
    """İkili aramanın kaç kez ortadaki elemana baktığını sayar."""
    adim = 0
    alt = 0
    ust = len(sirali) - 1
    while alt <= ust:
        adim = adim + 1
        orta = (alt + ust) // 2
        if sirali[orta] == hedef:
            break
        elif sirali[orta] < hedef:
            alt = orta + 1
        else:
            ust = orta - 1
    return adim


if __name__ == "__main__":
    for boyut in [10, 1_000, 1_000_000]:
        sayilar = list(range(boyut))
        aranan = -1  # Listede olmayan bir değer: en kötü durum
        print(
            f"n={boyut:>9}: doğrusal {dogrusal_adim(sayilar, aranan):>9} adım, "
            f"ikili {ikili_adim(sayilar, aranan):>3} adım"
        )
