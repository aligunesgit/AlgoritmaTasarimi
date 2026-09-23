"""M10 - Doğrusal aramanın bir çeşidi: bir değerin geçtiği TÜM indeksleri bulmak."""


def tum_konumlari_bul(liste: list[int], hedef: int) -> list[int]:
    """`hedef` değerinin listede geçtiği bütün indeksleri artan sırada, yeni bir liste olarak döndürür.

    Değer hiç yoksa boş liste döndürür. Girdi listesi değiştirilmez.
    """
    konumlar: list[int] = []
    for i in range(len(liste)):
        if liste[i] == hedef:
            konumlar.append(i)  # ilk bulduğumuzda durmuyoruz, taramaya devam
    return konumlar


if __name__ == "__main__":
    zarlar = [3, 6, 1, 6, 2, 6, 4]
    print("6 gelen atışlar:", tum_konumlari_bul(zarlar, 6))
